"""Auto-generated tests ensuring every metric module loads and exposes METRIC_META."""
from __future__ import annotations
import importlib
import pytest

CASES = [
    ("consumer_driven_contract_testing", "pact_contract_verification__consumer_contract_pass_rate", "Pact Contract Verification", "Consumer Contract Pass Rate"),
    ("contract_reliability", "openapi_contract_testing__contract_conformance_rate", "OpenAPI Contract Testing", "Contract Conformance Rate"),
    ("interface_reliability", "api_availability_testing__api_uptime", "API Availability Testing", "API Uptime %"),
    ("response_integrity_testing", "payload_accuracy_validation__payload_accuracy_score", "Payload Accuracy Validation", "Payload Accuracy Score"),
    ("schema_drift_detection", "breaking_change_detection__schema_drift_frequency", "Breaking Change Detection", "Schema Drift Frequency"),
]

@pytest.mark.parametrize('tech_slug,module_name,classification,metric', CASES)
def test_metric_module_metadata(tech_slug, module_name, classification, metric):
    mod = importlib.import_module(f"l2_fixtures.techniques.{tech_slug}.{module_name}")
    meta = mod.METRIC_META
    assert meta["l4_classification"] == classification
    assert meta["l5_metric"] == metric
    assert "primary_tool" in meta
    assert "secondary_tool" in meta
