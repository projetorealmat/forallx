#!/usr/bin/env python3
"""Fail when an editorial source still contains an explicit placeholder."""

from __future__ import annotations

import re
import sys
from pathlib import Path


SOURCE_SUFFIXES = {".tex", ".sty", ".bib"}
PLACEHOLDER_RE = re.compile(
    r"(?i)(?<![A-Z])(?:TODO|FIXME|TBD)(?![A-Z])|\\todo\b|<\s*placeholder\s*>"
)
SKIP_DIRECTORIES = {".git", "build", "_build", "out"}


def iter_sources(root: Path):
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in SOURCE_SUFFIXES:
            continue
        if any(part in SKIP_DIRECTORIES for part in path.relative_to(root).parts):
            continue
        yield path


def find_placeholders(root: Path) -> list[str]:
    findings: list[str] = []
    for path in iter_sources(root):
        for line_number, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), start=1):
            if PLACEHOLDER_RE.search(line):
                findings.append(f"{path.relative_to(root)}:{line_number}: {line.strip()}")
    return findings


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    findings = find_placeholders(root)
    if findings:
        print("Marcadores editoriais provisórios encontrados:")
        print("\n".join(f"- {finding}" for finding in findings))
        return 1
    print("Nenhum marcador editorial provisório encontrado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
