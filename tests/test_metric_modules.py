"""Auto-generated tests ensuring every metric module loads and exposes METRIC_META."""
from __future__ import annotations
import importlib
import pytest

CASES = [
    ("iac_security_scanning", "open_security_group_rule_detection__open_firewall_rule_count_iac", "Open Security Group Rule Detection", "Open Firewall Rule Count (IaC)"),
    ("iac_security_scanning", "unencrypted_storage_definition__unencrypted_storage_count_iac", "Unencrypted Storage Definition", "Unencrypted Storage Count (IaC)"),
    ("iac_security_scanning", "publicly_exposed_resource_detection__public_storage_bucket_count_iac", "Publicly Exposed Resource Detection", "Public Storage Bucket Count (IaC)"),
    ("iac_security_scanning", "cis_benchmark_compliance__cis_benchmark_violation_count_iac", "CIS Benchmark Compliance", "CIS Benchmark Violation Count (IaC)"),
    ("lint_rule_violations", "rule_detection_test__violation_density_per_kloc", "Rule Detection Test", "Violation Density per KLOC"),
    ("lint_rule_violations", "unused_variable_detection__resource_waste_identification", "Unused Variable Detection", "Resource Waste Identification"),
    ("lint_rule_violations", "naming_convention_validation__semantic_consistency_score", "Naming Convention Validation", "Semantic Consistency Score"),
    ("lint_rule_violations", "code_style_rule_validation__syntactic_uniformity_score", "Code Style Rule Validation", "Syntactic Uniformity Score"),
    ("lint_rule_violations", "complexity_rule_detection__structural_threshold_monitoring", "Complexity Rule Detection", "Structural Threshold Monitoring"),
    ("lint_rule_violations", "rule_severity_classification__impact_prioritization", "Rule Severity Classification", "Impact Prioritization"),
    ("lint_rule_violations", "multiple_violations_detection__aggregated_risk_assessment", "Multiple Violations Detection", "Aggregated Risk Assessment"),
    ("lint_rule_violations", "false_positive_prevention__accuracy_tuning", "False Positive Prevention", "Accuracy Tuning"),
    ("lint_rule_violations", "custom_rule_validation__project_specific_enforcement", "Custom Rule Validation", "Project-Specific Enforcement"),
    ("lint_rule_violations", "configuration_file_handling__environment_standardization", "Configuration File Handling", "Environment Standardization"),
    ("lint_rule_violations", "cicd_integration_validation__automated_gatekeeping", "CI/CD Integration Validation", "Automated Gatekeeping"),
    ("lint_rule_violations", "violation_reporting_validation__quality_audit_trail", "Violation Reporting Validation", "Quality Audit Trail"),
    ("secret_detection", "hardcoded_secret_scan__secrets_exposed_in_code_count", "Hardcoded Secret Scan", "Secrets Exposed in Code Count"),
    ("secret_detection", "pre_commit_secret_prevention__blocked_secret_commit_count", "Pre-Commit Secret Prevention", "Blocked Secret Commit Count"),
]

@pytest.mark.parametrize('tech_slug,module_name,classification,metric', CASES)
def test_metric_module_metadata(tech_slug, module_name, classification, metric):
    mod = importlib.import_module(f"l2_fixtures.techniques.{tech_slug}.{module_name}")
    meta = mod.METRIC_META
    assert meta["l4_classification"] == classification
    assert meta["l5_metric"] == metric
    assert "primary_tool" in meta
    assert "secondary_tool" in meta
