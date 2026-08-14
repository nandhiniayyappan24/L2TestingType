"""Auto-generated tests ensuring every metric module loads and exposes METRIC_META."""
from __future__ import annotations
import importlib
import pytest

CASES = [
    ("code_churn", "risk_based_testing_prioritization__code_churn_score", "Risk-Based Testing Prioritization", "Code Churn Score"),
    ("code_churn", "regression_testing_focus__impact_driven_verification", "Regression Testing Focus", "Impact-Driven Verification"),
    ("code_churn", "defect_prediction__fault_probability_modeling", "Defect Prediction", "Fault Probability Modeling"),
    ("code_churn", "test_case_maintenance_identification__validation_suite_updates", "Test Case Maintenance Identification", "Validation Suite Updates"),
    ("code_churn", "change_impact_analysis__side_effect_mapping", "Change Impact Analysis", "Side Effect Mapping"),
]

@pytest.mark.parametrize('tech_slug,module_name,classification,metric', CASES)
def test_metric_module_metadata(tech_slug, module_name, classification, metric):
    mod = importlib.import_module(f"l2_fixtures.techniques.{tech_slug}.{module_name}")
    meta = mod.METRIC_META
    assert meta["l4_classification"] == classification
    assert meta["l5_metric"] == metric
    assert "primary_tool" in meta
    assert "secondary_tool" in meta
