#!/usr/bin/env python3
"""Write computed statistics into README.md between HTML-comment markers.

Kept as a standalone script rather than an inline heredoc so the publish step
can re-run it after rebasing onto a freshly fetched branch. Only the marker
contents are touched, so a concurrent edit elsewhere in the README survives.

Expects these environment variables:
    REPOS, FOLLOWERS, FORKS, STARS, UPDATED
"""

from __future__ import annotations

import os
import re
import sys

PAIRED = ("REPOS", "FOLLOWERS", "FORKS", "STARS")
README = "README.md"


def main() -> int:
    try:
        values = {key: os.environ[key] for key in PAIRED}
        updated = os.environ["UPDATED"]
    except KeyError as exc:
        sys.exit(f"Missing required environment variable: {exc}")

    with open(README, encoding="utf-8") as handle:
        content = handle.read()

    missing: list[str] = []

    for key, value in values.items():
        marker = re.compile(
            r"(<!--STAT:{k}-->)(.*?)(<!--/STAT:{k}-->)".format(k=key), re.DOTALL
        )
        if not marker.search(content):
            missing.append(key)
            continue
        content = marker.sub(r"\g<1>" + value + r"\g<3>", content)

    # The timestamp sits in a standalone comment so it never renders.
    stamp = re.compile(r"(<!-- stats last updated: )([^>]*?)( -->)")
    if not stamp.search(content):
        missing.append("UPDATED")
    else:
        content = stamp.sub(r"\g<1>" + updated + r"\g<3>", content)

    if missing:
        sys.exit(f"Missing markers in {README}: " + ", ".join(missing))

    with open(README, "w", encoding="utf-8") as handle:
        handle.write(content)

    print(f"{README} updated with {values}, updated={updated}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
