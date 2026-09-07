#!/usr/bin/env python3
"""Regression checks for release status and catalog path policies."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = (ROOT / ".github" / "workflows" / "release-pdf.yml").read_text(encoding="utf-8")
POLICY = (ROOT / "RELEASE.md").read_text(encoding="utf-8")
DISPATCH = ROOT / "scripts" / "build_catalog_dispatch.py"

assert "--prerelease" in WORKFLOW, "v0 releases must be created as pre-releases"
assert "--prerelease=false" in WORKFLOW, "stable releases must explicitly clear pre-release status"
assert "pre-release" in POLICY, "release policy must document automatic pre-release enforcement"


def test_catalog_dispatch_uses_versioned_pdf_path() -> None:
    environment = os.environ.copy()
    environment.update(
        {
            "RELEASE_TAG": "v0.1.1",
            "RELEASE_STATUS": "em revisão",
            "GITHUB_REPOSITORY": "projetorealmat/forallx",
            "PDF_SHA256": "0" * 64,
        }
    )
    result = subprocess.run(
        [sys.executable, str(DISPATCH)],
        check=True,
        capture_output=True,
        text=True,
        env=environment,
    )
    payload = json.loads(result.stdout)
    book = payload["client_payload"]["book"]
    expected = "/assets/books/forallx/v0.1.1/forallx.pdf"
    assert book["pdf_path"] == expected, (
        f"catalog PDF path must be versioned, got {book['pdf_path']!r}"
    )


test_catalog_dispatch_uses_versioned_pdf_path()
