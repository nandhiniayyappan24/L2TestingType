"""Auto-generated tests ensuring every metric module loads and exposes METRIC_META."""
from __future__ import annotations
import importlib
import pytest

CASES = [
    ("cognitive_complexity", "maintainability_evaluation__technical_debt_impact", "Maintainability Evaluation", "Technical Debt Impact"),
    ("cognitive_complexity", "testability_analysis__unit_test_complexity", "Testability Analysis", "Unit Test Complexity"),
    ("cognitive_complexity", "risk_detection__defect_probability", "Risk Detection", "Defect Probability"),
    ("cognitive_complexity", "refactoring_guidance__modularization_opportunity", "Refactoring Guidance", "Modularization Opportunity"),
    ("cognitive_complexity", "code_review_support__reviewer_fatigue_factor", "Code Review Support", "Reviewer Fatigue Factor"),
    ("cognitive_complexity", "testing_effort_prioritization__qa_resource_allocation", "Testing Effort Prioritization", "QA Resource Allocation"),
    ("cognitive_complexity", "code_understandability_analysis__human_cognitive_load", "Code Understandability Analysis", "Human Cognitive Load"),
]

@pytest.mark.parametrize('tech_slug,module_name,classification,metric', CASES)
def test_metric_module_metadata(tech_slug, module_name, classification, metric):
    mod = importlib.import_module(f"l2_fixtures.techniques.{tech_slug}.{module_name}")
    meta = mod.METRIC_META
    assert meta["l4_classification"] == classification
    assert meta["l5_metric"] == metric
    assert "primary_tool" in meta
    assert "secondary_tool" in meta
