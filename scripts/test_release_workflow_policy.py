#!/usr/bin/env python3
"""Regression checks for the local book/central release workflow contract."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT / ".realmat" / "book.json").read_text(encoding="utf-8"))
PREPARE = (ROOT / ".github" / "workflows" / "prepare-release-pr.yml").read_text(encoding="utf-8")
PUBLISH = (ROOT / ".github" / "workflows" / "release-pdf.yml").read_text(encoding="utf-8")
LATEX = (ROOT / ".github" / "workflows" / "latex.yml").read_text(encoding="utf-8")
README = (ROOT / "README.md").read_text(encoding="utf-8")
CITATION = (ROOT / "CITATION.cff").read_text(encoding="utf-8")


assert CONFIG["id"] == "forallx"
assert CONFIG["pdf_name"] == "forallx.pdf"
assert CONFIG["tex_entrypoint"] == "forallx.tex"
assert CONFIG["portal_repository"] == "projetorealmat/projetorealmat.github.io"

assert "workflow_dispatch:" in PREPARE
assert "projetorealmat/.github/.github/workflows/book-prepare-release.yml@v1" in PREPARE
assert "config: .realmat/book.json" in PREPARE
assert "secrets: inherit" in PREPARE

assert "pull_request:" in PUBLISH and "- closed" in PUBLISH
assert "workflow_dispatch:" in PUBLISH
assert "projetorealmat/.github/.github/workflows/book-publish-release.yml@v1" in PUBLISH
assert "secrets: inherit" in PUBLISH

for legacy_name in ("REALMAT_AUTOMATION_TOKEN", "PORTAL_DISPATCH_TOKEN"):
    assert legacy_name not in PREPARE + PUBLISH, f"legacy credential remains: {legacy_name}"

assert "Reservar versionamento para Release PR" in LATEX
assert "version/date-released só podem mudar em uma Release PR" in LATEX
assert r"release/v\d+\.\d+\.\d+" in LATEX
assert "current_release_date < base_release_date" in LATEX
assert "  push:\n    branches:" not in LATEX

match = re.search(
    r'^version:\s*["\']?([0-9]+\.[0-9]+\.[0-9]+)["\']?\s*$',
    CITATION,
    re.MULTILINE,
)
assert match is not None
current_tag = f"v{match.group(1)}"
assert f"/releases/download/{current_tag}/forallx.pdf" in README
assert f"({current_tag})" in README
assert f"A versão atualmente recomendada é `{current_tag}`" in README

print("book release workflow contract passed")
