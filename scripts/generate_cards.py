#!/usr/bin/env python3
"""Render GitHub analytics cards as static SVGs committed to this repository.

Public instances of github-readme-stats share a single API token and routinely
return an error card ("Maximum retries exceeded") with HTTP 200, which makes the
failure invisible to status-code checks. Generating the cards here removes that
dependency entirely: the data comes from the authenticated GITHUB_TOKEN and the
output is a plain SVG in the repo, so it cannot rate-limit or go offline.

Usage:
    GITHUB_TOKEN=... ACCOUNT=CloudTechDevOps python3 scripts/generate_cards.py
"""

from __future__ import annotations

import collections
import json
import os
import sys
import urllib.error
import urllib.request

API = "https://api.github.com/graphql"

# Palette matched to banner.svg / skills-orbit.svg
BG_FROM = "#020617"
BG_TO = "#1e1b4b"
STROKE = "#334155"
TITLE = "#67e8f9"
LABEL = "#94a3b8"
VALUE = "#e0f2fe"
ACCENT = "#a78bfa"

QUERY = """
query($login: String!) {
  user(login: $login) {
    name
    followers { totalCount }
    following { totalCount }
    contributionsCollection {
      totalCommitContributions
      totalPullRequestContributions
      totalIssueContributions
      restrictedContributionsCount
      contributionCalendar { totalContributions }
    }
    pullRequests(states: MERGED) { totalCount }
    repositories(first: 100, ownerAffiliations: OWNER) {
      totalCount
      nodes {
        isFork
        stargazerCount
        forkCount
        languages(first: 15, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name color } }
        }
      }
    }
  }
}
"""


def graphql(token: str, login: str) -> dict:
    body = json.dumps({"query": QUERY, "variables": {"login": login}}).encode()
    req = urllib.request.Request(
        API,
        data=body,
        headers={
            "Authorization": f"bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "profile-card-generator",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        payload = json.load(resp)
    if "errors" in payload:
        raise SystemExit(f"GraphQL error: {payload['errors']}")
    if not payload.get("data", {}).get("user"):
        raise SystemExit(f"No data returned for user {login!r}")
    return payload["data"]["user"]


def esc(text: str) -> str:
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def collect(user: dict) -> tuple[dict, list]:
    repos = user["repositories"]
    contrib = user["contributionsCollection"]

    # Totals span every public repository so these figures agree with the
    # "By the Numbers" table in README.md.
    stars = sum(r["stargazerCount"] for r in repos["nodes"])
    forks = sum(r["forkCount"] for r in repos["nodes"])

    # Language bytes deliberately exclude forks: upstream code in a fork is not
    # this account's work and would skew the breakdown.
    totals = collections.Counter()
    colors: dict[str, str] = {}
    for repo in repos["nodes"]:
        if repo.get("isFork"):
            continue
        for edge in repo["languages"]["edges"]:
            name = edge["node"]["name"]
            totals[name] += edge["size"]
            colors[name] = edge["node"]["color"] or ACCENT

    grand = sum(totals.values()) or 1
    languages = [
        (name, size, 100.0 * size / grand, colors[name])
        for name, size in totals.most_common(6)
    ]

    stats = {
        "Total Contributions": contrib["contributionCalendar"]["totalContributions"],
        "Commits (past year)": contrib["totalCommitContributions"],
        "Pull Requests": user["pullRequests"]["totalCount"],
        "Stars Earned": stars,
        "Community Forks": forks,
        "Public Repositories": repos["totalCount"],
        "Followers": user["followers"]["totalCount"],
        "Code Written": f"{grand / 1_000_000:.2f} MB",
    }
    return stats, languages


def defs(prefix: str) -> str:
    return f"""  <defs>
    <linearGradient id="{prefix}bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{BG_FROM}"/>
      <stop offset="100%" stop-color="{BG_TO}"/>
    </linearGradient>
  </defs>"""


def stats_card(stats: dict, account: str) -> str:
    rows = list(stats.items())
    pad, top, line_h = 26, 74, 30
    height = top + line_h * len(rows) + 16
    width = 460

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" '
        f'aria-label="GitHub statistics for {esc(account)}">',
        f"<title>GitHub statistics for {esc(account)}</title>",
        defs("s"),
        f'  <rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="12" '
        f'fill="url(#sbg)" stroke="{STROKE}"/>',
        f'  <text x="{pad}" y="36" fill="{TITLE}" font-family="Segoe UI,Helvetica,Arial,sans-serif" '
        f'font-size="17" font-weight="600">GitHub Statistics</text>',
        f'  <rect x="{pad}" y="50" width="{width - 2 * pad}" height="1" fill="{STROKE}"/>',
    ]
    for i, (label, value) in enumerate(rows):
        y = top + i * line_h
        parts.append(
            f'  <text x="{pad}" y="{y}" fill="{LABEL}" '
            f'font-family="Segoe UI,Helvetica,Arial,sans-serif" font-size="13">{esc(label)}</text>'
        )
        parts.append(
            f'  <text x="{width - pad}" y="{y}" fill="{VALUE}" text-anchor="end" '
            f'font-family="Segoe UI,Helvetica,Arial,sans-serif" font-size="14" '
            f'font-weight="600">{esc(value)}</text>'
        )
    parts.append("</svg>")
    return "\n".join(parts)


def languages_card(languages: list, account: str) -> str:
    pad, top, line_h = 26, 84, 30
    width = 460
    height = top + line_h * len(languages) + 16
    bar_x, bar_w = 150, width - 150 - pad - 52

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" '
        f'aria-label="Most used languages for {esc(account)}">',
        f"<title>Most used languages for {esc(account)}</title>",
        defs("l"),
        f'  <rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="12" '
        f'fill="url(#lbg)" stroke="{STROKE}"/>',
        f'  <text x="{pad}" y="36" fill="{TITLE}" font-family="Segoe UI,Helvetica,Arial,sans-serif" '
        f'font-size="17" font-weight="600">Most Used Languages</text>',
        f'  <rect x="{pad}" y="50" width="{width - 2 * pad}" height="1" fill="{STROKE}"/>',
    ]

    # Stacked summary bar
    x = float(pad)
    total_pct = sum(p for _, _, p, _ in languages) or 1
    usable = width - 2 * pad
    for name, _size, pct, color in languages:
        seg = usable * pct / total_pct
        parts.append(
            f'  <rect x="{x:.1f}" y="60" width="{max(seg, 0.8):.1f}" height="7" '
            f'fill="{color}"><title>{esc(name)} {pct:.1f}%</title></rect>'
        )
        x += seg

    for i, (name, _size, pct, color) in enumerate(languages):
        y = top + i * line_h
        parts.append(f'  <circle cx="{pad + 5}" cy="{y - 4}" r="5" fill="{color}"/>')
        parts.append(
            f'  <text x="{pad + 18}" y="{y}" fill="{LABEL}" '
            f'font-family="Segoe UI,Helvetica,Arial,sans-serif" font-size="13">{esc(name)}</text>'
        )
        parts.append(
            f'  <rect x="{bar_x}" y="{y - 10}" width="{bar_w}" height="8" rx="4" fill="#0f172a"/>'
        )
        parts.append(
            f'  <rect x="{bar_x}" y="{y - 10}" width="{max(bar_w * pct / 100, 2):.1f}" '
            f'height="8" rx="4" fill="{color}"/>'
        )
        parts.append(
            f'  <text x="{width - pad}" y="{y}" fill="{VALUE}" text-anchor="end" '
            f'font-family="Segoe UI,Helvetica,Arial,sans-serif" font-size="13" '
            f'font-weight="600">{pct:.1f}%</text>'
        )
    parts.append("</svg>")
    return "\n".join(parts)


def write(path: str, content: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(content + "\n")
    print(f"wrote {path} ({len(content)} bytes)")


def main() -> int:
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        sys.exit("GITHUB_TOKEN (or GH_TOKEN) is required")
    account = os.environ.get("ACCOUNT", "CloudTechDevOps")

    try:
        user = graphql(token, account)
    except urllib.error.HTTPError as exc:
        sys.exit(f"GitHub API returned {exc.code}: {exc.read()[:300]!r}")

    stats, languages = collect(user)
    if not languages:
        sys.exit("No language data returned — refusing to write an empty card")

    print("stats:", stats)
    print("languages:", [(n, f"{p:.1f}%") for n, _s, p, _c in languages])

    write("assets/stats-card.svg", stats_card(stats, account))
    write("assets/languages-card.svg", languages_card(languages, account))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
