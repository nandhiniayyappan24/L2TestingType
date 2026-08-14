"""Auto-generated tests ensuring every metric module loads and exposes METRIC_META."""
from __future__ import annotations
import importlib
import pytest

CASES = [
    ("code_duplication", "defect_propagation_risk_detection__multi_point_failure_probability", "Defect Propagation Risk Detection", "Multi-Point Failure Probability"),
    ("code_duplication", "refactoring_identification__redundancy_localization", "Refactoring Identification", "Redundancy Localization"),
    ("code_duplication", "code_quality_assessment__structural_cleanliness_score", "Code Quality Assessment", "Structural Cleanliness Score"),
    ("code_duplication", "test_maintenance_reduction__test_suite_streamlining", "Test Maintenance Reduction", "Test Suite Streamlining"),
    ("code_duplication", "refactoring_opportunity_detection__abstraction_potential", "Refactoring Opportunity Detection", "Abstraction Potential"),
    ("code_duplication", "risk_based_testing_prioritization__regression_focus_mapping", "Risk-Based Testing Prioritization", "Regression Focus Mapping"),
    ("code_duplication", "maintainability_testing__synchronization_verification", "Maintainability Testing", "Synchronization Verification"),
]

@pytest.mark.parametrize('tech_slug,module_name,classification,metric', CASES)
def test_metric_module_metadata(tech_slug, module_name, classification, metric):
    mod = importlib.import_module(f"l2_fixtures.techniques.{tech_slug}.{module_name}")
    meta = mod.METRIC_META
    assert meta["l4_classification"] == classification
    assert meta["l5_metric"] == metric
    assert "primary_tool" in meta
    assert "secondary_tool" in meta
