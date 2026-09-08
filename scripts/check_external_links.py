#!/usr/bin/env python3
"""Check external links used by the operational book documentation."""

from __future__ import annotations

import os
import re
import sys
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
# CUSTOMIZATIONS.md contains a historical bibliography of external editions.
# Those references are useful, but their availability should not block CI.
FILES = (
    ROOT / "README.md",
    ROOT / "RELEASE.md",
    ROOT / "CONTRIBUTING.md",
    ROOT / "CITATION.cff",
)
URL_RE = re.compile(r"""https?://[^\s)<>"']+""")
TRAILING = ".,;:!?]}>'"
USER_AGENT = "Mozilla/5.0 (compatible; REALMat-link-check/1.0)"


def urls_from_files() -> list[str]:
    found: set[str] = set()
    for path in FILES:
        if not path.exists():
            continue
        content = path.read_text(encoding="utf-8", errors="replace")
        for raw in URL_RE.findall(content):
            found.add(raw.rstrip(TRAILING))
    return sorted(found)


def citation_version() -> str:
    text = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    match = re.search(
        r'''^version:\s*["']?([0-9]+\.[0-9]+\.[0-9]+)["']?\s*$''',
        text,
        re.MULTILINE,
    )
    if match is None:
        raise RuntimeError("CITATION.cff não contém uma versão semântica válida.")
    return match.group(1)


def pending_release_url() -> str | None:
    """Return the expected PDF URL while a matching Release PR is still open."""
    head_ref = os.environ.get("GITHUB_HEAD_REF", "")
    match = re.fullmatch(r"release/v([0-9]+\.[0-9]+\.[0-9]+)", head_ref)
    if match is None:
        return None

    version = citation_version()
    if match.group(1) != version:
        return None

    return (
        "https://github.com/projetorealmat/forallx/releases/download/"
        f"v{version}/forallx.pdf"
    )


def request_status(url: str) -> int:
    headers = {"User-Agent": USER_AGENT}
    try:
        request = Request(url, headers=headers, method="HEAD")
        with urlopen(request, timeout=25) as response:
            return response.status
    except HTTPError:
        # Alguns servidores respondem incorretamente a HEAD; confirme por GET.
        pass
    except (URLError, TimeoutError):
        pass

    request = Request(url, headers=headers, method="GET")
    with urlopen(request, timeout=25) as response:
        response.read(1024)
        return response.status


def main() -> int:
    failures: list[tuple[str, str]] = []
    urls = urls_from_files()
    pending_url = pending_release_url()
    print(f"Checking {len(urls)} external links...")

    for url in urls:
        if url == pending_url:
            print(f"PENDING release asset: {url}")
            continue

        try:
            status = request_status(url)
            if not 200 <= status < 400:
                failures.append((url, f"HTTP {status}"))
                print(f"FAIL {status}: {url}")
            else:
                print(f"OK {status}: {url}")
        except Exception as error:  # noqa: BLE001 - report the concrete URL failure
            failures.append((url, str(error)))
            print(f"FAIL {url}: {error}")
        time.sleep(0.15)

    if failures:
        print("\nExternal link checks failed:")
        for url, reason in failures:
            print(f"- {url}: {reason}")
        return 1

    print("All external links are reachable or are pending publication in this Release PR.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
