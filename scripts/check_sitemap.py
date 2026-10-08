"""Validate built sitemap, canonical/hreflang, gzip and optional live HTTP status."""

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import gzip
from functools import partial
from html.parser import HTMLParser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urljoin, urlsplit
from urllib.request import HTTPRedirectHandler, build_opener
import xml.etree.ElementTree as ET
from threading import Thread


class Head(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.canonical = []
        self.alternates = {}
        self.feed(html.split("</head>")[0])

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical.append(attrs["href"])
        if tag == "link" and attrs.get("rel") == "alternate" and "hreflang" in attrs:
            self.alternates[attrs["hreflang"]] = attrs["href"]


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--live", action="store_true")
    parser.add_argument("--local-http", action="store_true")
    parser.add_argument("--site-dir", default="site")
    args = parser.parse_args()
    site = Path(args.site_dir)
    base = "https://ivan-bdgilko.github.io/BeeApiary_Docs/"
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9", "x": "http://www.w3.org/1999/xhtml"}
    data = (site / "sitemap.xml").read_bytes()
    root = ET.fromstring(data)
    assert gzip.decompress((site / "sitemap.xml.gz").read_bytes()) == data
    entries = {node.findtext("s:loc", namespaces=ns): node for node in root}
    assert len(entries) == len(root)
    counts, dates = Counter(), Counter()
    for url, node in entries.items():
        assert url.startswith(base)
        relative = url[len(base):]
        p = site / relative / "index.html" if url.endswith("/") else site / relative
        head = Head(p.read_text(encoding="utf-8"))
        assert head.canonical == [url], (url, head.canonical)
        alternates = {link.attrib["hreflang"]: link.attrib["href"] for link in node.findall("x:link", ns)}
        assert {k: urljoin(url, v) for k, v in head.alternates.items()} == alternates, url
        for lang, target in alternates.items():
            assert target in entries, (url, target)
            other = {link.attrib["hreflang"]: link.attrib["href"] for link in entries[target].findall("x:link", ns)}
            assert other == alternates, (url, target, "non-reciprocal hreflang")
        assert node.find("s:changefreq", ns) is None
        assert node.find("s:priority", ns) is None
        first = relative.split("/")[0]
        counts[first if first in ("en", "de", "es", "fr", "pl", "pt-BR", "tr") else "uk"] += 1
        dates[node.findtext("s:lastmod", namespaces=ns)] += 1
    assert len(counts) == 8
    # All fallback pages must canonicalize to an indexed source; 404 is excluded.
    for lang in counts:
        folder = site if lang == "uk" else site / lang
        for source in Path("docs/uk").rglob("*.md"):
            topic = source.relative_to("docs/uk")
            destination = topic.parent if topic.name in ("index.md", "README.md") else topic.with_suffix("")
            p = folder / destination / "index.html"
            head = Head(p.read_text(encoding="utf-8"))
            assert len(head.canonical) == 1 and head.canonical[0] in entries, p
            actual_locale = lang if (Path("docs") / lang / topic).is_file() else "uk"
            prefix = "" if actual_locale == "uk" else actual_locale + "/"
            suffix = "" if destination.as_posix() == "." else destination.as_posix() + "/"
            assert head.canonical == [base + prefix + suffix], p
    assert f"Sitemap: {base}sitemap.xml" in (site / "robots.txt").read_text()
    print("Canonical URLs:", len(entries), dict(counts))
    print("Unique Git dates:", len([d for d in dates if d]), "undated:", dates[None])
    print("XML/gzip, targets, canonical and reciprocal hreflang: PASS")
    if args.local_http:
        class QuietHandler(SimpleHTTPRequestHandler):
            def log_message(self, *args):
                pass
        server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(site)))
        thread = Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            for url in entries:
                local = f"http://127.0.0.1:{server.server_port}/" + url[len(base):]
                with build_opener(NoRedirect).open(local, timeout=10) as response:
                    assert response.status == 200, url
            print("Local HTTP: all", len(entries), "URLs return 200 without redirects")
        finally:
            server.shutdown()
            server.server_close()
    if args.live:
        def check(url):
            try:
                with build_opener(NoRedirect).open(url, timeout=30) as response:
                    return url, response.status
            except Exception as error:
                return url, str(error)
        with ThreadPoolExecutor(max_workers=8) as pool:
            results = list(pool.map(check, entries))
        failures = [(url, status) for url, status in results if status != 200]
        print("Live HTTP:", len(results) - len(failures), "200; failures:", failures[:20])
        origin = urlsplit(base)
        for url in (base + "sitemap.xml", base + "robots.txt", f"{origin.scheme}://{origin.netloc}/robots.txt"):
            print("Live endpoint:", check(url))
        if failures:
            raise SystemExit(1)


if __name__ == "__main__":
    main()
