"""Auto-generated tests ensuring every metric module loads and exposes METRIC_META."""
from __future__ import annotations
import importlib
import pytest

CASES = [
    ("algorithmic_complexity", "complexity_based_performance_risk__cyclomatic_complexity_performance_hotspots", "Complexity-Based Performance Risk", "Cyclomatic Complexity (Performance Hotspots)"),
    ("algorithmic_complexity", "big_o_complexity_review__nested_loop_depth_count", "Big-O Complexity Review", "Nested Loop Depth Count"),
    ("build_performance", "build_time_regression__build_duration_seconds", "Build Time Regression", "Build Duration (seconds)"),
    ("bundle_size_analysis", "unused_dependency_detection__unused_import_count", "Unused Dependency Detection", "Unused Import Count"),
    ("concurrency_analysis", "thread_safety_pattern_detection__race_condition_risk_count", "Thread-Safety Pattern Detection", "Race Condition Risk Count"),
    ("database_query_analysis", "n1_query_pattern_detection__n1_query_anti_pattern_count", "N+1 Query Pattern Detection", "N+1 Query Anti-Pattern Count"),
    ("dependency_graph_analysis", "circular_dependency_detection__circular_dependency_count", "Circular Dependency Detection", "Circular Dependency Count"),
    ("memory_management", "memory_allocation_pattern_analysis__large_allocation_in_loop_count", "Memory Allocation Pattern Analysis", "Large Allocation in Loop Count"),
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
