"""Auto-generated tests ensuring every metric module loads and exposes METRIC_META."""
from __future__ import annotations
import importlib
import pytest

CASES = [
    ("api_endpoint_validation", "unauthenticated_endpoint_testing__unauthenticated_api_endpoint_count", "Unauthenticated Endpoint Testing", "Unauthenticated API Endpoint Count"),
    ("authorization_testing", "bola_idor_testing__bola_finding_count", "BOLA / IDOR Testing", "BOLA Finding Count"),
    ("pii_in_api_responses", "pii_exposure_in_live_responses__pii_in_api_response_count", "PII Exposure in Live Responses", "PII in API Response Count"),
    ("rate_limiting_compliance", "rate_limit_enforcement_testing__apis_without_rate_limiting_count", "Rate Limit Enforcement Testing", "APIs Without Rate Limiting Count"),
    ("session_management_testing", "session_timeout_compliance__session_timeout_compliance_rate", "Session Timeout Compliance", "Session Timeout Compliance Rate"),
    ("transport_security", "security_header_validation__missing_security_header_count", "Security Header Validation", "Missing Security Header Count"),
    ("transport_security", "tls_configuration_testing__weak_tls_config_count", "TLS Configuration Testing", "Weak TLS Config Count"),
]

@pytest.mark.parametrize('tech_slug,module_name,classification,metric', CASES)
def test_metric_module_metadata(tech_slug, module_name, classification, metric):
    mod = importlib.import_module(f"l2_fixtures.techniques.{tech_slug}.{module_name}")
    meta = mod.METRIC_META
    assert meta["l4_classification"] == classification
    assert meta["l5_metric"] == metric
    assert "primary_tool" in meta
    assert "secondary_tool" in meta
