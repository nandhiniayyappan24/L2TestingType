"""Auto-generated tests ensuring every metric module loads and exposes METRIC_META."""
from __future__ import annotations
import importlib
import pytest

CASES = [
    ("coverage_delta", "regression_testing_monitoring__coverage_delta", "Regression Testing Monitoring", "Coverage Delta %"),
    ("coverage_delta", "test_suite_effectiveness_tracking__discovery_power_assessment", "Test Suite Effectiveness Tracking", "Discovery Power Assessment"),
    ("coverage_delta", "cicd_quality_gate_enforcement__deployment_readiness_guard", "CI/CD Quality Gate Enforcement", "Deployment Readiness Guard"),
    ("coverage_delta", "change_impact_analysis__ripple_effect_mapping", "Change Impact Analysis", "Ripple Effect Mapping"),
    ("coverage_delta", "new_code_testing_validation__fresh_logic_proofing", "New Code Testing Validation", "Fresh Logic Proofing"),
    ("coverage_delta", "quality_improvement_measurement__structural_health_benchmarking", "Quality Improvement Measurement", "Structural Health Benchmarking"),
]

@pytest.mark.parametrize('tech_slug,module_name,classification,metric', CASES)
def test_metric_module_metadata(tech_slug, module_name, classification, metric):
    mod = importlib.import_module(f"l2_fixtures.techniques.{tech_slug}.{module_name}")
    meta = mod.METRIC_META
    assert meta["l4_classification"] == classification
    assert meta["l5_metric"] == metric
    assert "primary_tool" in meta
    assert "secondary_tool" in meta
