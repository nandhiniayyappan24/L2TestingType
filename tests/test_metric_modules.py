"""Auto-generated tests ensuring every metric module loads and exposes METRIC_META."""
from __future__ import annotations
import importlib
import pytest

CASES = [
    ("change_management_testing", "change_control_verification__unreviewed_change_count", "Change Control Verification", "Unreviewed Change Count"),
    ("iac_security_scanning", "open_security_group_rule_detection__open_firewall_rule_count_iac", "Open Security Group Rule Detection", "Open Firewall Rule Count (IaC)"),
    ("iac_security_scanning", "unencrypted_storage_definition__unencrypted_storage_count_iac", "Unencrypted Storage Definition", "Unencrypted Storage Count (IaC)"),
    ("iac_security_scanning", "publicly_exposed_resource_detection__public_storage_bucket_count_iac", "Publicly Exposed Resource Detection", "Public Storage Bucket Count (IaC)"),
    ("iac_security_scanning", "cis_benchmark_compliance__cis_benchmark_violation_count_iac", "CIS Benchmark Compliance", "CIS Benchmark Violation Count (IaC)"),
    ("pii_logging_detection", "pii_in_log_statements__pii_log_statement_count", "PII in Log Statements", "PII Log Statement Count"),
    ("secret_detection", "hardcoded_secret_scan__secrets_exposed_in_code_count", "Hardcoded Secret Scan", "Secrets Exposed in Code Count"),
    ("secret_detection", "pre_commit_secret_prevention__blocked_secret_commit_count", "Pre-Commit Secret Prevention", "Blocked Secret Commit Count"),
    ("secret_management", "secrets_in_repo_history__historical_secret_exposure_count", "Secrets in Repo History", "Historical Secret Exposure Count"),
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
