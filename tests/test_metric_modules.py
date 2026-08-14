"""Auto-generated tests ensuring every metric module loads and exposes METRIC_META."""
from __future__ import annotations
import importlib
import pytest

CASES = [
    ("build_performance", "build_time_regression__build_duration_seconds", "Build Time Regression", "Build Duration (seconds)"),
    ("bundle_size_analysis", "unused_dependency_detection__unused_import_count", "Unused Dependency Detection", "Unused Import Count"),
    ("dependency_graph_analysis", "circular_dependency_detection__circular_dependency_count", "Circular Dependency Detection", "Circular Dependency Count"),
]

@pytest.mark.parametrize('tech_slug,module_name,classification,metric', CASES)
def test_metric_module_metadata(tech_slug, module_name, classification, metric):
    mod = importlib.import_module(f"l2_fixtures.techniques.{tech_slug}.{module_name}")
    meta = mod.METRIC_META
    assert meta["l4_classification"] == classification
    assert meta["l5_metric"] == metric
    assert "primary_tool" in meta
    assert "secondary_tool" in meta
