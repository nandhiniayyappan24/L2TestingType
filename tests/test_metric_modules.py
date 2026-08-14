"""Auto-generated tests ensuring every metric module loads and exposes METRIC_META."""
from __future__ import annotations
import importlib
import pytest

CASES = [
    ("consent_age_gate_compliance", "coppa_age_verification_testing__age_gate_bypass_count", "COPPA Age Verification Testing", "Age-Gate Bypass Count"),
    ("cookie_consent_testing", "cookie_consent_compliance__non_consented_tracker_count", "Cookie Consent Compliance", "Non-Consented Tracker Count"),
    ("data_subject_rights_testing", "right_to_erasure_testing__data_deletion_verification_rate", "Right-to-Erasure Testing", "Data Deletion Verification Rate"),
    ("pii_in_api_responses", "pii_exposure_in_live_responses__pii_in_api_response_count", "PII Exposure in Live Responses", "PII in API Response Count"),
]

@pytest.mark.parametrize('tech_slug,module_name,classification,metric', CASES)
def test_metric_module_metadata(tech_slug, module_name, classification, metric):
    mod = importlib.import_module(f"l2_fixtures.techniques.{tech_slug}.{module_name}")
    meta = mod.METRIC_META
    assert meta["l4_classification"] == classification
    assert meta["l5_metric"] == metric
    assert "primary_tool" in meta
    assert "secondary_tool" in meta
