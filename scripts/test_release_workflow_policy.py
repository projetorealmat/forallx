#!/usr/bin/env python3
"""Regression checks for release status, Release PR, and catalog path policies."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = (ROOT / ".github" / "workflows" / "release-pdf.yml").read_text(encoding="utf-8")
PREPARE_WORKFLOW = (ROOT / ".github" / "workflows" / "prepare-release-pr.yml").read_text(
    encoding="utf-8"
)
LATEX_WORKFLOW = (ROOT / ".github" / "workflows" / "latex.yml").read_text(encoding="utf-8")
POLICY = (ROOT / "RELEASE.md").read_text(encoding="utf-8")
DISPATCH = ROOT / "scripts" / "build_catalog_dispatch.py"

assert "--prerelease" in WORKFLOW, "v0 releases must be created as pre-releases"
assert "--prerelease=false" in WORKFLOW, "stable releases must explicitly clear pre-release status"
assert "pre-release" in POLICY, "release policy must document automatic pre-release enforcement"

# Release intent must be explicit: a merged Release PR, not a metadata-only push.
assert "pull_request:" in WORKFLOW and "- closed" in WORKFLOW, (
    "release publication must react to a closed pull request"
)
assert "github.event.pull_request.merged == true" in WORKFLOW, (
    "only a successfully merged Release PR may publish"
)
assert "startsWith(github.event.pull_request.head.ref, 'release/v')" in WORKFLOW, (
    "release publication must require the release/v* branch convention"
)
assert "github.event.pull_request.head.repo.full_name == github.repository" in WORKFLOW, (
    "a publishing Release PR must originate in the repository itself"
)
assert 'expected_branch="release/${release_tag}"' in WORKFLOW, (
    "the Release PR branch must match the version declared in CITATION.cff"
)
assert 'git show "${RELEASE_COMMIT}^:CITATION.cff"' in WORKFLOW, (
    "the workflow must verify that the Release PR changed the Citation version"
)
assert 'git tag -a "${RELEASE_TAG}" "${RELEASE_COMMIT}"' in WORKFLOW, (
    "the workflow must create the release tag only after final validation/build"
)
assert 'git push origin "refs/tags/${RELEASE_TAG}"' in WORKFLOW, (
    "the workflow must push the generated release tag"
)
assert "--draft" in WORKFLOW, (
    "the GitHub Release must be assembled as a draft before publication"
)

# Release PR preparation is itself automated and auditable.
assert "workflow_dispatch:" in PREPARE_WORKFLOW, (
    "Release PR preparation must be an explicit manually requested workflow"
)
assert "release/${release_tag}" in PREPARE_WORKFLOW, (
    "the preparation workflow must use a release/v* branch"
)
assert "CITATION.cff" in PREPARE_WORKFLOW and "date-released" in PREPARE_WORKFLOW, (
    "the Release PR must carry release metadata"
)
assert "gh pr create" in PREPARE_WORKFLOW, (
    "the preparation workflow must open the Release PR automatically"
)
assert "Release PR" in POLICY, (
    "the release policy must document Release PR as the publication model"
)

# Ordinary PRs may edit citation metadata, but release version/date are reserved.
assert "Reservar versionamento para Release PR" in LATEX_WORKFLOW, (
    "CI must explicitly protect release version/date changes"
)
assert "version/date-released só podem mudar em uma Release PR" in LATEX_WORKFLOW, (
    "ordinary PRs must not be able to change release version/date"
)
assert r"release/v\d+\.\d+\.\d+" in LATEX_WORKFLOW, (
    "Release PR validation must enforce the release/vMAJOR.MINOR.PATCH branch format"
)

# The ordinary PDF check must not duplicate the final publication build on main pushes.
assert "  push:\n    branches:" not in LATEX_WORKFLOW, (
    "the ordinary PDF workflow must not duplicate the publication build on main pushes"
)


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
