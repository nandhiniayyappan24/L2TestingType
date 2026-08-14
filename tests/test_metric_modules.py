"""Auto-generated tests ensuring every metric module loads and exposes METRIC_META."""
from __future__ import annotations
import importlib
import pytest

CASES = [
    ("secret_scanning", "hardcoded_secret_detection__secrets_exposed_in_code_count", "Hardcoded Secret Detection", "Secrets Exposed in Code Count"),
    ("secret_scanning", "pre_commit_secret_prevention__blocked_secret_commit_count", "Pre-Commit Secret Prevention", "Blocked Secret Commit Count"),
    ("secret_scanning", "secrets_in_git_history__historical_secret_exposure_count", "Secrets in Git History", "Historical Secret Exposure Count"),
]

@pytest.mark.parametrize('tech_slug,module_name,classification,metric', CASES)
def test_metric_module_metadata(tech_slug, module_name, classification, metric):
    mod = importlib.import_module(f"l2_fixtures.techniques.{tech_slug}.{module_name}")
    meta = mod.METRIC_META
    assert meta["l4_classification"] == classification
    assert meta["l5_metric"] == metric
    assert "primary_tool" in meta
    assert "secondary_tool" in meta
