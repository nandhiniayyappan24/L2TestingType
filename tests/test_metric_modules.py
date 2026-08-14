"""Auto-generated tests ensuring every metric module loads and exposes METRIC_META."""
from __future__ import annotations
import importlib
import pytest

CASES = [
    ("authentication_authorization_testing", "broken_access_control_testing__unauthorized_access_count", "Broken Access Control Testing", "Unauthorized Access Count"),
    ("dast_dynamic_application_security_testing", "owasp_top_10_vulnerability_scan__owasp_highcritical_finding_count", "OWASP Top 10 Vulnerability Scan", "OWASP High/Critical Finding Count"),
    ("dast_dynamic_application_security_testing", "sql_injection_testing__sqli_vulnerability_count", "SQL Injection Testing", "SQLi Vulnerability Count"),
    ("dast_dynamic_application_security_testing", "xss_testing__xss_vulnerability_count", "XSS Testing", "XSS Vulnerability Count"),
    ("dast_dynamic_application_security_testing", "server_side_request_forgery_ssrf_testing__ssrf_vulnerability_count", "Server-Side Request Forgery (SSRF) Testing", "SSRF Vulnerability Count"),
]

@pytest.mark.parametrize('tech_slug,module_name,classification,metric', CASES)
def test_metric_module_metadata(tech_slug, module_name, classification, metric):
    mod = importlib.import_module(f"l2_fixtures.techniques.{tech_slug}.{module_name}")
    meta = mod.METRIC_META
    assert meta["l4_classification"] == classification
    assert meta["l5_metric"] == metric
    assert "primary_tool" in meta
    assert "secondary_tool" in meta
