"""Auto-generated tests ensuring every metric module loads and exposes METRIC_META."""
from __future__ import annotations
import importlib
import pytest

CASES = [
    ("technical_debt", "code_churn_in_performance_critical_paths__churn_score_performance_modules", "Code Churn in Performance-Critical Paths", "Churn Score (Performance Modules)"),
    ("test_coverage", "performance_test_code_coverage__performance_test_coverage", "Performance Test Code Coverage", "Performance Test Coverage %"),
]

@pytest.mark.parametrize('tech_slug,module_name,classification,metric', CASES)
def test_metric_module_metadata(tech_slug, module_name, classification, metric):
    mod = importlib.import_module(f"l2_fixtures.techniques.{tech_slug}.{module_name}")
    meta = mod.METRIC_META
    assert meta["l4_classification"] == classification
    assert meta["l5_metric"] == metric
    assert "primary_tool" in meta
    assert "secondary_tool" in meta
