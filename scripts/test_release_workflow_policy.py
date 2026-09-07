#!/usr/bin/env python3
"""Regression checks for release status policy."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = (ROOT / ".github" / "workflows" / "release-pdf.yml").read_text(encoding="utf-8")
POLICY = (ROOT / "RELEASE.md").read_text(encoding="utf-8")

assert "--prerelease" in WORKFLOW, "v0 releases must be created as pre-releases"
assert "--prerelease=false" in WORKFLOW, "stable releases must explicitly clear pre-release status"
assert "pre-release" in POLICY, "release policy must document automatic pre-release enforcement"
