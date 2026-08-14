"""Auto-generated tests ensuring every metric module loads and exposes METRIC_META."""
from __future__ import annotations
import importlib
import pytest

CASES = [
    ("iac_scanning", "open_security_group_rule_detection__open_firewall_rule_count", "Open Security Group Rule Detection", "Open Firewall Rule Count"),
    ("iac_scanning", "unencrypted_storage_definition__unencrypted_storage_count", "Unencrypted Storage Definition", "Unencrypted Storage Count"),
    ("iac_scanning", "publicly_exposed_resource_detection__public_storage_bucket_count", "Publicly Exposed Resource Detection", "Public Storage Bucket Count"),
    ("iac_scanning", "cis_benchmark_compliance__cis_benchmark_violation_count", "CIS Benchmark Compliance", "CIS Benchmark Violation Count"),
]

@pytest.mark.parametrize('tech_slug,module_name,classification,metric', CASES)
def test_metric_module_metadata(tech_slug, module_name, classification, metric):
    mod = importlib.import_module(f"l2_fixtures.techniques.{tech_slug}.{module_name}")
    meta = mod.METRIC_META
    assert meta["l4_classification"] == classification
    assert meta["l5_metric"] == metric
    assert "primary_tool" in meta
    assert "secondary_tool" in meta
