"""Auto-generated tests ensuring every metric module loads and exposes METRIC_META."""
from __future__ import annotations
import importlib
import pytest

CASES = [
    ("dom_interaction_validation", "element_interaction_testing__interaction_success_rate", "Element Interaction Testing", "Interaction Success Rate"),
    ("visual_regression_testing", "screenshot_comparison__visual_regression_failure_rate", "Screenshot Comparison", "Visual Regression Failure Rate"),
]

@pytest.mark.parametrize('tech_slug,module_name,classification,metric', CASES)
def test_metric_module_metadata(tech_slug, module_name, classification, metric):
    mod = importlib.import_module(f"l2_fixtures.techniques.{tech_slug}.{module_name}")
    meta = mod.METRIC_META
    assert meta["l4_classification"] == classification
    assert meta["l5_metric"] == metric
    assert "primary_tool" in meta
    assert "secondary_tool" in meta
