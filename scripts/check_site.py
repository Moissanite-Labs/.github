#!/usr/bin/env python3
"""Validate the published tree without third-party dependencies or network access."""

from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1] / "docs"
errors = []


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.ids = set()
        self.refs = []
        self.h1 = 0
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            if attrs["id"] in self.ids:
                errors.append(f"{self.path.name}: duplicate id {attrs['id']}")
            self.ids.add(attrs["id"])
        if tag == "h1":
            self.h1 += 1
        if tag == "img" and "alt" not in attrs:
            errors.append(f"{self.path.name}: image has no alt attribute")
        for attr in ("href", "src"):
            if attr in attrs:
                self.refs.append(attrs[attr])
        if tag == "meta" and attrs.get("property") == "og:image":
            self.refs.append(attrs["content"])


def check_reference(source, ref):
    url = urlsplit(ref)
    if url.netloc == "moissanite-labs.github.io" and url.path.startswith("/.github/"):
        return check_reference(ROOT / "index.html", url.path.removeprefix("/.github/"))
    if url.scheme or url.netloc:
        if url.scheme not in {"https", "mailto", "tel", "data"}:
            errors.append(f"{source.name}: unexpected URL scheme: {ref}")
        return
    if url.path.startswith("/"):
        errors.append(f"{source.name}: root-relative path breaks project hosting: {ref}")
        return
    target = (source.parent / unquote(url.path)).resolve() if url.path else source
    if not target.is_relative_to(ROOT):
        errors.append(f"{source.name}: reference escapes published tree: {ref}")
        return
    if target.is_dir():
        target /= "index.html"
    if not target.is_file():
        errors.append(f"{source.name}: missing local file: {ref}")
    elif url.fragment and target.suffix == ".html":
        page = pages.get(target)
        if page and unquote(url.fragment) not in page.ids:
            errors.append(f"{source.name}: missing anchor: {ref}")


assert (ROOT / "index.html").is_file(), "docs/index.html is missing"
pages = {path: Page(path) for path in ROOT.rglob("*.html")}
for path, page in pages.items():
    if page.h1 != 1:
        errors.append(f"{path.name}: expected one h1, found {page.h1}")
    for ref in page.refs:
        check_reference(path, ref)
for path in ROOT.rglob("*.css"):
    for ref in re.findall(r"url\(\s*['\"]?([^)'\"\s]+)", path.read_text()):
        check_reference(path, ref)
for path in ROOT.rglob("*.svg"):
    try:
        ET.parse(path)
    except ET.ParseError as error:
        errors.append(f"{path.name}: invalid SVG: {error}")

if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print(f"Site checks passed: {len(pages)} HTML pages; local links, anchors, CSS assets, and SVGs resolve.")
