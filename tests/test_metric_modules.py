"""Auto-generated tests ensuring every metric module loads and exposes METRIC_META."""
from __future__ import annotations
import importlib
import pytest

CASES = [
    ("consent_age_gate_compliance", "coppa_age_verification_testing__age_gate_bypass_count", "COPPA Age Verification Testing", "Age-Gate Bypass Count"),
    ("pii_logging_detection", "pii_in_log_statements__pii_log_statement_count", "PII in Log Statements", "PII Log Statement Count"),
    ("student_pii_exposure_scan", "pii_data_exposure_detection__pii_exposure_finding_count", "PII Data Exposure Detection", "PII Exposure Finding Count"),
    ("student_pii_exposure_scan", "pii_in_codebase_detection__pii_in_codebase_count", "PII in Codebase Detection", "PII in Codebase Count"),
]

@pytest.mark.parametrize('tech_slug,module_name,classification,metric', CASES)
def test_metric_module_metadata(tech_slug, module_name, classification, metric):
    mod = importlib.import_module(f"l2_fixtures.techniques.{tech_slug}.{module_name}")
    meta = mod.METRIC_META
    assert meta["l4_classification"] == classification
    assert meta["l5_metric"] == metric
    assert "primary_tool" in meta
    assert "secondary_tool" in meta
