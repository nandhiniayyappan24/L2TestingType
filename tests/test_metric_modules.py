"""Auto-generated tests ensuring every metric module loads and exposes METRIC_META."""
from __future__ import annotations
import importlib
import pytest

CASES = [
    ("cyclomatic_complexity", "static_analysis_metric__execution_path_integrity", "Static Analysis Metric", "Execution Path Integrity"),
    ("cyclomatic_complexity", "decision_coverage__decision_outcome_verification", "Decision Coverage", "Decision Outcome Verification"),
    ("cyclomatic_complexity", "condition_coverage__logical_sub_expression_validation", "Condition Coverage", "Logical Sub-expression Validation"),
    ("cyclomatic_complexity", "logic_coverage_metric__total_logical_combinatorial_coverage", "Logic Coverage Metric", "Total Logical Combinatorial Coverage"),
    ("cyclomatic_complexity", "maintainability_analysis__technical_debt_impact", "Maintainability Analysis", "Technical Debt Impact"),
    ("cyclomatic_complexity", "test_prioritization__qa_resource_allocation", "Test Prioritization", "QA Resource Allocation"),
]

@pytest.mark.parametrize('tech_slug,module_name,classification,metric', CASES)
def test_metric_module_metadata(tech_slug, module_name, classification, metric):
    mod = importlib.import_module(f"l2_fixtures.techniques.{tech_slug}.{module_name}")
    meta = mod.METRIC_META
    assert meta["l4_classification"] == classification
    assert meta["l5_metric"] == metric
    assert "primary_tool" in meta
    assert "secondary_tool" in meta
