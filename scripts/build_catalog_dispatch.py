#!/usr/bin/env python3
"""Build the payload used to propose a portal catalog update."""

from __future__ import annotations

import json
import os
import re


VERSION_RE = re.compile(r"^v(\d+)\.(\d+)\.(\d+)$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


def expected_status(tag: str) -> str:
    match = VERSION_RE.fullmatch(tag)
    if match is None:
        raise SystemExit("A release tag must follow vMAJOR.MINOR.PATCH.")
    major, minor, patch = (int(part) for part in match.groups())
    if major == 0:
        return "em revisão"
    if major == 1 and minor == 0 and patch == 0:
        return "tradução aprovada"
    if major == 1:
        return "versão revisada"
    return "nova versão"


def main() -> int:
    tag = os.environ["RELEASE_TAG"]
    repository = os.environ["GITHUB_REPOSITORY"]
    status = os.environ["RELEASE_STATUS"]
    digest = os.environ["PDF_SHA256"]

    if status != expected_status(tag):
        raise SystemExit(f"Status {status!r} incompatível com {tag}.")
    if not SHA256_RE.fullmatch(digest):
        raise SystemExit("PDF_SHA256 não é um digest SHA-256 válido.")

    book = {
        "id": "forallx",
        "title": "forallx: Lógica",
        "short_title": "forallx",
        "subject": "lógica formal",
        "version": tag,
        "status": status,
        "repository": repository,
        "ref": tag,
        "release_url": f"https://github.com/{repository}/releases/tag/{tag}",
        "pdf_url": f"https://github.com/{repository}/releases/download/{tag}/forallx.pdf",
        "pdf_path": "/assets/books/forallx.pdf",
        "sha256": digest,
        "release_date": os.environ.get("RELEASE_DATE", ""),
    }
    print(json.dumps({"event_type": "book-release", "client_payload": {"book": book}}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
