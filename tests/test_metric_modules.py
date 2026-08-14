"""Auto-generated tests ensuring every metric module loads and exposes METRIC_META."""
from __future__ import annotations
import importlib
import pytest

CASES = [
    ("access_control", "privileged_access_audit__overprivileged_account_count", "Privileged Access Audit", "Overprivileged Account Count"),
    ("audit_evidence_completeness", "soc_2_evidence_collection_rate__evidence_collection_rate", "SOC 2 Evidence Collection Rate", "Evidence Collection Rate %"),
    ("change_management_testing", "change_control_verification__unreviewed_change_count", "Change Control Verification", "Unreviewed Change Count"),
    ("secret_management", "secrets_in_repo_history__historical_secret_exposure_count", "Secrets in Repo History", "Historical Secret Exposure Count"),
]

@pytest.mark.parametrize('tech_slug,module_name,classification,metric', CASES)
def test_metric_module_metadata(tech_slug, module_name, classification, metric):
    mod = importlib.import_module(f"l2_fixtures.techniques.{tech_slug}.{module_name}")
    meta = mod.METRIC_META
    assert meta["l4_classification"] == classification
    assert meta["l5_metric"] == metric
    assert "primary_tool" in meta
    assert "secondary_tool" in meta
