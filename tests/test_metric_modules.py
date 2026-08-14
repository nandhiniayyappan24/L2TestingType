"""Auto-generated tests ensuring every metric module loads and exposes METRIC_META."""
from __future__ import annotations
import importlib
import pytest

CASES = [
    ("dependency_risk_sca", "transitive_dependency_analysis__hidden_relationship_mapping", "Transitive Dependency Analysis", "Hidden Relationship Mapping"),
    ("dependency_risk_sca", "license_compliance_testing__legal_risk_validation", "License Compliance Testing", "Legal Risk Validation"),
    ("dependency_risk_sca", "supply_chain_security_analysis__trust_integrity_verification", "Supply Chain Security Analysis", "Trust Integrity Verification"),
    ("dependency_risk_sca", "dependency_health_monitoring__community_vitality_tracking", "Dependency Health Monitoring", "Community Vitality Tracking"),
    ("dependency_risk_sca", "risk_prioritization__mitigation_effort_ranking", "Risk Prioritization", "Mitigation Effort Ranking"),
    ("dependency_risk_sca", "continuous_dependency_monitoring__real_time_alerting", "Continuous Dependency Monitoring", "Real-Time Alerting"),
    ("dependency_risk_sca", "vulnerability_dependency_detection__known_cve_count", "Vulnerability Dependency Detection", "Known CVE Count"),
    ("dependency_risk_sca", "outdated_dependency_detection__version_lag_assessment", "Outdated Dependency Detection", "Version Lag Assessment"),
    ("static_vulnerabilities_sast", "secure_coding_validation__best_practice_compliance", "Secure Coding Validation", "Best Practice Compliance"),
    ("static_vulnerabilities_sast", "input_validation_testing__entry_point_sanitization", "Input Validation Testing", "Entry Point Sanitization"),
    ("static_vulnerabilities_sast", "data_flow_security_analysis__sensitive_information_tracking", "Data Flow Security Analysis", "Sensitive Information Tracking"),
    ("static_vulnerabilities_sast", "authentication_authorization_weakness_detection__access_control_verification", "Authentication & Authorization Weakness Detection", "Access Control Verification"),
    ("static_vulnerabilities_sast", "dependency_library_vulnerability_detection__supply_chain_security", "Dependency & Library Vulnerability Detection", "Supply Chain Security"),
    ("static_vulnerabilities_sast", "compliance_security_standard_validation__regulatory_alignment", "Compliance & Security Standard Validation", "Regulatory Alignment"),
    ("static_vulnerabilities_sast", "security_vulnerability_detection__exploit_surface_identification", "Security Vulnerability Detection", "Exploit Surface Identification"),
]

@pytest.mark.parametrize('tech_slug,module_name,classification,metric', CASES)
def test_metric_module_metadata(tech_slug, module_name, classification, metric):
    mod = importlib.import_module(f"l2_fixtures.techniques.{tech_slug}.{module_name}")
    meta = mod.METRIC_META
    assert meta["l4_classification"] == classification
    assert meta["l5_metric"] == metric
    assert "primary_tool" in meta
    assert "secondary_tool" in meta
