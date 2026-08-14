"""Auto-generated tests ensuring every metric module loads and exposes METRIC_META."""
from __future__ import annotations
import importlib
import pytest

CASES = [
    ("api_endpoint_validation", "unauthenticated_endpoint_testing__unauthenticated_api_endpoint_count", "Unauthenticated Endpoint Testing", "Unauthenticated API Endpoint Count"),
    ("audit_evidence_completeness", "soc_2_evidence_collection_rate__evidence_collection_rate", "SOC 2 Evidence Collection Rate", "Evidence Collection Rate %"),
    ("authentication_authorization_testing", "broken_access_control_testing__unauthorized_access_count", "Broken Access Control Testing", "Unauthorized Access Count"),
    ("authorization_testing", "bola_idor_testing__bola_finding_count", "BOLA / IDOR Testing", "BOLA Finding Count"),
    ("change_management_testing", "change_control_verification__unreviewed_change_count", "Change Control Verification", "Unreviewed Change Count"),
    ("consent_age_gate_compliance", "coppa_age_verification_testing__age_gate_bypass_count", "COPPA Age Verification Testing", "Age-Gate Bypass Count"),
    ("cookie_consent_testing", "cookie_consent_compliance__non_consented_tracker_count", "Cookie Consent Compliance", "Non-Consented Tracker Count"),
    ("dast_dynamic_application_security_testing", "owasp_top_10_vulnerability_scan__owasp_highcritical_finding_count", "OWASP Top 10 Vulnerability Scan", "OWASP High/Critical Finding Count"),
    ("dast_dynamic_application_security_testing", "sql_injection_testing__sqli_vulnerability_count", "SQL Injection Testing", "SQLi Vulnerability Count"),
    ("dast_dynamic_application_security_testing", "xss_testing__xss_vulnerability_count", "XSS Testing", "XSS Vulnerability Count"),
    ("data_subject_rights_testing", "right_to_erasure_testing__data_deletion_verification_rate", "Right-to-Erasure Testing", "Data Deletion Verification Rate"),
    ("pii_in_api_responses", "pii_exposure_in_live_responses__pii_in_api_response_count", "PII Exposure in Live Responses", "PII in API Response Count"),
    ("payment_data_security", "cardholder_data_exposure_scan__chd_exposure_finding_count", "Cardholder Data Exposure Scan", "CHD Exposure Finding Count"),
    ("rate_limiting_compliance", "rate_limit_enforcement_testing__apis_without_rate_limiting_count", "Rate Limit Enforcement Testing", "APIs Without Rate Limiting Count"),
    ("session_management_testing", "session_timeout_compliance__session_timeout_compliance_rate", "Session Timeout Compliance", "Session Timeout Compliance Rate"),
    ("tlsencryption_compliance", "tls_configuration_testing__weak_tls_config_count", "TLS Configuration Testing", "Weak TLS Config Count"),
    ("transport_security", "security_header_validation__missing_security_header_count", "Security Header Validation", "Missing Security Header Count"),
]

@pytest.mark.parametrize('tech_slug,module_name,classification,metric', CASES)
def test_metric_module_metadata(tech_slug, module_name, classification, metric):
    mod = importlib.import_module(f"l2_fixtures.techniques.{tech_slug}.{module_name}")
    meta = mod.METRIC_META
    assert meta["l4_classification"] == classification
    assert meta["l5_metric"] == metric
    assert "primary_tool" in meta
    assert "secondary_tool" in meta
