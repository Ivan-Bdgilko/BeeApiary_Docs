"""Defer only the lower homepage photo until it is near the viewport."""

import base64
from html import escape
from html.parser import HTMLParser
from pathlib import PurePosixPath
from urllib.parse import urlsplit


PHOTOS = {"beeapiary-system-components.webp", "beeapiary-system-components.jpeg"}
SVG = '<svg xmlns="http://www.w3.org/2000/svg" width="1079" height="754"></svg>'
PLACEHOLDER = "data:image/svg+xml;base64," + base64.b64encode(SVG.encode()).decode()
INITIALIZE = """(()=>{const photo=document.currentScript.previousElementSibling;
const reveal=()=>{photo.loading="eager";photo.src=photo.dataset.deferredSrc;photo.removeAttribute("data-deferred-src")};
if(!("IntersectionObserver" in window)){reveal();return}
try{const observer=new IntersectionObserver(entries=>{if(entries.some(entry=>entry.isIntersecting)){observer.unobserve(photo);reveal()}},{rootMargin:"300px 0px",threshold:0});observer.observe(photo)}catch{reveal()}})();"""


class PhotoFinder(HTMLParser):
    def __init__(self, content):
        super().__init__()
        self.matches = []
        self.feed(content)

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == "img" and PurePosixPath(urlsplit(attrs.get("src", "")).path).name in PHOTOS:
            self.matches.append((self.get_starttag_text(), attrs))


def on_page_content(html, page, config, files):
    if page.file.norm_src_uri != "index.md":
        return html
    matches = PhotoFinder(html).matches
    if not matches:
        return html
    if len(matches) != 1:
        raise ValueError("Expected exactly one lower homepage photo")
    original, attrs = matches[0]
    if (attrs.get("width"), attrs.get("height")) != ("1079", "754"):
        raise ValueError("Homepage photo dimensions changed; update its placeholder")
    attrs["data-deferred-src"] = attrs["src"]
    attrs["src"] = PLACEHOLDER
    attrs["loading"] = "eager"
    attrs["fetchpriority"] = "low"
    placeholder = "<img " + " ".join(
        f'{key}="{escape(value, quote=True)}"' if value is not None else key
        for key, value in attrs.items()
    ) + ">"
    replacement = (
        placeholder + "<script>" + INITIALIZE + "</script>"
        '<noscript><style>img[data-deferred-src]{display:none!important}</style>'
        + original + "</noscript>"
    )
    return html.replace(original, replacement, 1)
