"""Auto-generated tests ensuring every metric module loads and exposes METRIC_META."""
from __future__ import annotations
import importlib
import pytest

CASES = [
    ("mutation_score", "fault_detection_capability__logic_error_sensitivity", "Fault Detection Capability", "Logic Error Sensitivity"),
    ("mutation_score", "test_coverage_quality_validation__test_rigor_assessment", "Test Coverage Quality Validation", "Test Rigor Assessment"),
    ("mutation_score", "test_case_improvement_identification__weak_spot_localization", "Test Case Improvement Identification", "Weak Spot Localization"),
    ("mutation_score", "edge_case_detection__boundary_mutant_analysis", "Edge Case Detection", "Boundary Mutant Analysis"),
]

@pytest.mark.parametrize('tech_slug,module_name,classification,metric', CASES)
def test_metric_module_metadata(tech_slug, module_name, classification, metric):
    mod = importlib.import_module(f"l2_fixtures.techniques.{tech_slug}.{module_name}")
    meta = mod.METRIC_META
    assert meta["l4_classification"] == classification
    assert meta["l5_metric"] == metric
    assert "primary_tool" in meta
    assert "secondary_tool" in meta
