#!/usr/bin/env python3
"""Refresh the "Latest Writing" list in README.md from the Medium RSS feed.

Only the text between the WRITING markers is replaced, so the rest of the
README is never touched. If the feed is unreachable or empty the README is left
as it is, rather than replacing real links with nothing.

Expects (optional) environment variables:
    MEDIUM_USER   Medium handle without the @ (default: veerababu.narni232)
    LIMIT         number of posts to list (default: 5)
"""

from __future__ import annotations

import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

README = "README.md"
START = "<!--WRITING:START-->"
END = "<!--WRITING:END-->"


def fetch(user: str) -> bytes:
    request = urllib.request.Request(
        f"https://medium.com/feed/@{user}",
        headers={"User-Agent": "CloudTechDevOps-profile-readme"},
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.read()


def main() -> int:
    user = os.environ.get("MEDIUM_USER", "veerababu.narni232")
    limit = int(os.environ.get("LIMIT", "5"))

    try:
        items = ET.fromstring(fetch(user)).findall("./channel/item")
    except Exception as exc:  # network or XML problem: keep the current list
        print(f"::warning::Medium feed unavailable, README unchanged: {exc}")
        return 0

    lines = []
    for item in items[:limit]:
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").split("?")[0].strip()
        if not title or not link:
            continue
        stamp = item.findtext("pubDate")
        date = parsedate_to_datetime(stamp).strftime("%b %Y") if stamp else ""
        title = title.replace("[", "(").replace("]", ")")
        lines.append(f"- [{title}]({link})" + (f" <sub>· {date}</sub>" if date else ""))

    if not lines:
        print("::warning::Medium feed had no posts, README unchanged")
        return 0

    with open(README, encoding="utf-8") as handle:
        content = handle.read()

    block = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    if not block.search(content):
        sys.exit(f"Missing {START} / {END} markers in {README}")

    content = block.sub(lambda _: START + "\n" + "\n".join(lines) + "\n" + END, content)

    with open(README, "w", encoding="utf-8") as handle:
        handle.write(content)

    print(f"{README} updated with {len(lines)} posts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
