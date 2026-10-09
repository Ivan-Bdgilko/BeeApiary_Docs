"""Guard the agreed image and self-hosted font changes in generated HTML."""

import argparse
import base64
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET


class Resources(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.images = {}
        self.styles = []
        self.deferred = []
        self.fallbacks = []
        self.in_noscript = False
        self.feed(html)

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == "noscript":
            self.in_noscript = True
        if tag == "img":
            self.images[Path(attrs.get("src", "")).name] = attrs
            if "data-deferred-src" in attrs:
                self.deferred.append(attrs)
            if self.in_noscript:
                self.fallbacks.append(attrs)
        if tag == "link" and attrs.get("rel") == "stylesheet":
            self.styles.append(attrs["href"])

    def handle_endtag(self, tag):
        if tag == "noscript":
            self.in_noscript = False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-dir", default="site")
    parser.add_argument("--fonts", action="store_true")
    args = parser.parse_args()
    site = Path(args.site_dir)
    for lang in ("uk", "en", "de", "es", "fr", "pl", "pt-BR", "tr"):
        page = site / ("index.html" if lang == "uk" else f"{lang}/index.html")
        resources = Resources(page.read_text(encoding="utf-8"))
        for name, size in {
            "beeapiary-emblem.png": (780, 780),
            "beeapiary-connectivity-overview.webp": (1448, 1086),
            "beeapiary-system-components.webp": (1079, 754),
        }.items():
            attrs = resources.images[name]
            assert (attrs.get("width"), attrs.get("height")) == tuple(map(str, size)), (lang, name)
        assert resources.images["beeapiary-connectivity-overview.webp"]["loading"] == "eager"
        assert resources.images["beeapiary-connectivity-overview.webp"]["fetchpriority"] == "high"
        photo = resources.images["beeapiary-system-components.webp"]
        assert photo["loading"] == "lazy" and photo["decoding"] == "async"
        assert len(resources.deferred) == 1 and resources.fallbacks == [photo], lang
        deferred = resources.deferred[0]
        assert deferred["data-deferred-src"] == photo["src"]
        assert (page.parent / unquote(photo["src"])).is_file()
        assert deferred["loading"] == "eager" and deferred["fetchpriority"] == "low"
        assert all(deferred.get(key) == photo.get(key) for key in ("alt", "class", "width", "height", "decoding"))
        assert deferred["src"].startswith("data:image/svg+xml;base64,")
        svg = ET.fromstring(base64.b64decode(deferred["src"].split(",", 1)[1]))
        assert svg.tag == "{http://www.w3.org/2000/svg}svg" and len(svg) == 0
        assert (svg.get("width"), svg.get("height")) == ("1079", "754")
        if args.fonts:
            assert all(not urlsplit(href).hostname for href in resources.styles), lang
            font_css = []
            for href in resources.styles:
                path = page.parent / unquote(href)
                text = path.read_text(encoding="utf-8")
                if "@font-face" in text:
                    font_css.append(text)
                    assert "font-display: fallback" in text
                    for url in re.findall(r"url\(([^)]+)\)", text):
                        target = url.strip("\"'")
                        assert not urlsplit(target).hostname, target
                        assert (path.parent / unquote(target)).is_file(), target
            assert font_css and all(family in "".join(font_css) for family in ("Roboto", "Roboto Mono")), lang
    print("Eight homepages: dimensions, LCP priority, deferred photo/noscript PASS" + ("; local font CSS/files PASS" if args.fonts else ""))


if __name__ == "__main__":
    main()
