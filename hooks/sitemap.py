"""Accurate sitemap dates and canonical language variants; no build-date fallback."""

from datetime import datetime
import gzip
import logging
from pathlib import Path
import re
import subprocess
import xml.etree.ElementTree as ET

from mkdocs.plugins import event_priority

log = logging.getLogger("mkdocs.hooks.sitemap")
ROOT = Path(__file__).resolve().parents[1]
DATES = {}
LANGUAGES = []
BASE = ""
PAGES = {}


def git(*args):
    return subprocess.check_output(
        ["git", *args], cwd=ROOT, encoding="utf-8", errors="strict"
    )


def significant(lines):
    """Ignore blank lines, trailing whitespace, and translation workflow status."""
    return [
        line.rstrip() for line in lines
        if line.strip() and not line.startswith("translation_status:")
    ]


def history_dates(history):
    dates, aliases = {}, {}
    for commit in history.split("__SITEMAP_DATE__")[1:]:
        date, _, patch = commit.partition("\n")
        # Validate Git's ISO date; retain timezone, including per-page dates.
        date = datetime.fromisoformat(date.strip()).isoformat()
        for diff in patch.split("diff --git ")[1:]:
            header, _, body = diff.partition("\n")
            match = re.fullmatch(r"a/(.+) b/(.+)", header)
            if not match:
                continue
            old, new = match.groups()
            target = aliases.get(new, new)
            added, removed = [], []
            for line in body.splitlines():
                if line.startswith("+") and not line.startswith("+++ "):
                    added.append(line[1:])
                elif line.startswith("-") and not line.startswith("--- "):
                    removed.append(line[1:])
            if significant(added) != significant(removed):
                dates.setdefault(target, date)
            if old != new:
                aliases[old] = target
    return dates


def on_config(config):
    global DATES, LANGUAGES, BASE
    BASE = config.site_url.rstrip("/") + "/"
    LANGUAGES = [x.locale for x in config.plugins["i18n"].config.languages if x.build]
    DATES = {}
    try:
        if git("rev-parse", "--is-shallow-repository").strip() == "true":
            log.info("Shallow Git history: omitting sitemap lastmod")
            return config
        DATES = history_dates(git(
            "log", "--format=__SITEMAP_DATE__%cI", "--find-renames",
            "--diff-merges=first-parent", "--patch", "--", "docs"
        ))
        # Uncommitted/untracked sources do not have a reliable published date.
        dirty = git("diff", "--name-only", "HEAD", "--", "docs").splitlines()
        dirty += git("ls-files", "--others", "--exclude-standard", "--", "docs").splitlines()
        for path in dirty:
            DATES.pop(path, None)
    except (OSError, subprocess.CalledProcessError, ValueError):
        DATES = {}
        log.info("Git dates unavailable: omitting sitemap lastmod")
    return config


def on_pre_build(config):
    if not config.plugins["i18n"].building:
        PAGES.clear()


def page_url(topic, locale, default, use_directory_urls):
    path = Path(topic)
    if path.name in ("index.md", "README.md"):
        parent = path.parent.as_posix()
        url = ("" if parent == "." else parent) + "/"
    elif use_directory_urls:
        url = path.with_suffix("").as_posix() + "/"
    else:
        url = path.with_suffix(".html").as_posix()
    return BASE + ("" if locale == default else locale + "/") + url.lstrip("/")


@event_priority(-100)
def on_page_context(context, page, config, nav):
    file = page.file
    default = config.plugins["i18n"].default_language
    topic = file.norm_src_uri
    alternates = {
        lang: page_url(topic, lang, default, config.use_directory_urls)
        for lang in LANGUAGES
        if (ROOT / "docs" / lang / topic).is_file()
    }
    current = file.locale_alternate_of
    page.sitemap_include = (
        file.locale == current and not page.is_link
        and file.inclusion.is_included()
    )
    page.sitemap_alternates = alternates
    page.sitemap_lastmod = DATES.get(Path(file.abs_src_path).relative_to(ROOT).as_posix())
    page.canonical_url = alternates.get(current if page.sitemap_include else file.locale)
    if page.sitemap_include:
        PAGES[page.canonical_url] = (page.sitemap_lastmod, alternates)
    # Material uses extra.alternate for both head hreflang and its language selector.
    config.extra.alternate = [
        dict(alt, link=alternates[alt["lang"]])
        for alt in config.extra.alternate if alt["lang"] in alternates
    ]
    return context


@event_priority(-200)
def on_post_build(config):
    # i18n recursively builds languages at priority -100. Only validate after
    # that outer call completes, when the cumulative sitemap is available.
    if config.plugins["i18n"].building:
        return
    site = Path(config.site_dir)
    sitemap = site / "sitemap.xml"
    namespace = "http://www.sitemaps.org/schemas/sitemap/0.9"
    xhtml = "http://www.w3.org/1999/xhtml"
    ET.register_namespace("", namespace)
    ET.register_namespace("xhtml", xhtml)
    root = ET.Element(f"{{{namespace}}}urlset")
    for url, (date, alternates) in sorted(PAGES.items()):
        entry = ET.SubElement(root, f"{{{namespace}}}url")
        ET.SubElement(entry, f"{{{namespace}}}loc").text = url
        if date:
            ET.SubElement(entry, f"{{{namespace}}}lastmod").text = date
        for lang, href in alternates.items():
            ET.SubElement(entry, f"{{{xhtml}}}link", rel="alternate", hreflang=lang, href=href)
    urls = list(PAGES)
    if len(urls) != len(set(urls)):
        raise ValueError("Duplicate sitemap URLs")
    for url in urls:
        relative = url.removeprefix(BASE)
        target = site / relative / "index.html" if url.endswith("/") else site / relative
        if not url.startswith(BASE) or not target.is_file():
            raise ValueError(f"Sitemap target does not exist: {url}")
        html = target.read_text(encoding="utf-8")
        if f'rel="canonical" href="{url}"' not in html:
            raise ValueError(f"Sitemap URL is not canonical: {url}")
        if re.search(r'http-equiv=["\']refresh|name=["\']robots["\'][^>]*noindex', html, re.I):
            raise ValueError(f"Redirect/noindex page in sitemap: {url}")
    ET.indent(root)
    ET.ElementTree(root).write(sitemap, encoding="utf-8", xml_declaration=True)
    (site / "sitemap.xml.gz").write_bytes(gzip.compress(sitemap.read_bytes(), mtime=0))
    (site / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n", encoding="utf-8"
    )
    log.info("Validated %s canonical sitemap URLs", len(urls))
