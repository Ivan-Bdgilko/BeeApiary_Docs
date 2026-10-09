"""Guard the agreed image and self-hosted font changes in generated HTML."""

import argparse
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


class Resources(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.images = {}
        self.styles = []
        self.feed(html)

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == "img":
            self.images[Path(attrs.get("src", "")).name] = attrs
        if tag == "link" and attrs.get("rel") == "stylesheet":
            self.styles.append(attrs["href"])


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
    print("Eight homepages: dimensions/eager/lazy PASS" + ("; local font CSS/files PASS" if args.fonts else ""))


if __name__ == "__main__":
    main()
