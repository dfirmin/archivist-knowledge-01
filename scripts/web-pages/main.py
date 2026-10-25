"""Fetch web pages and add their readable text to the inbox."""
import html
import re
from html.parser import HTMLParser
from urllib.parse import urlparse

import requests

import knodex


class Text(HTMLParser):
    SKIP = {"script", "style", "nav", "footer", "header", "noscript", "svg"}

    def __init__(self):
        super().__init__()
        self.parts, self.skip, self.title = [], 0, ""
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.skip += 1
        if tag == "title":
            self._in_title = True
        if tag in ("p", "br", "li", "h1", "h2", "h3", "h4", "tr", "div"):
            self.parts.append("\n")
        if tag in ("h1", "h2", "h3"):
            self.parts.append("#" * int(tag[1]) + " ")
        if tag == "li":
            self.parts.append("- ")

    def handle_endtag(self, tag):
        if tag in self.SKIP and self.skip:
            self.skip -= 1
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        elif not self.skip:
            self.parts.append(data)


urls = [u.strip() for u in (knodex.inputs.get("urls") or "").split(",") if u.strip()]
if not urls:
    knodex.log("No URLs given. Set the urls input.")
for url in urls:
    u = urlparse(url)
    name = re.sub(r"[^a-z0-9]+", "-", (u.netloc + u.path).lower()).strip("-")[:80] + ".md"
    if knodex.inbox.exists(name):
        knodex.log("already brought in:", url)
        continue
    r = requests.get(url, timeout=30, headers={"User-Agent": "knodex-connector"})
    r.raise_for_status()
    p = Text()
    p.feed(r.text)
    text = re.sub(r"\n\s*\n+", "\n\n", html.unescape("".join(p.parts))).strip()
    title = " ".join(p.title.split()) or url
    knodex.inbox.add(name, f"# {title}\n\nSource: {url}\n\n{text}\n")
