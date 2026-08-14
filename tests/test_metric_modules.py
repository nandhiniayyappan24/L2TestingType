"""Auto-generated tests ensuring every metric module loads and exposes METRIC_META."""
from __future__ import annotations
import importlib
import pytest

CASES = [
    ("flow_assurance_confidence", "step_transition_testing__state_transition_accuracy", "Step Transition Testing", "State Transition Accuracy %"),
    ("input_boundary_validity", "minimum_boundary_testing__min_value_pass_rate", "Minimum Boundary Testing", "Min Value Pass Rate"),
    ("input_boundary_validity", "maximum_boundary_testing__max_value_pass_rate", "Maximum Boundary Testing", "Max Value Pass Rate"),
    ("input_boundary_validity", "just_outside_boundary_testing__out_of_range_rejection_rate", "Just-Outside Boundary Testing", "Out-of-Range Rejection Rate"),
    ("partition_class_coverage", "valid_partition_testing__valid_class_pass_rate", "Valid Partition Testing", "Valid Class Pass Rate"),
    ("transition_correctness", "valid_state_transition_testing__valid_transition_pass_rate", "Valid State Transition Testing", "Valid Transition Pass Rate"),
    ("user_journey_confidence", "critical_path_testing__critical_path_success_rate", "Critical Path Testing", "Critical Path Success Rate"),
    ("user_journey_confidence", "happy_path_testing__happy_path_pass_rate", "Happy Path Testing", "Happy Path Pass Rate"),
    ("user_journey_confidence", "end_to_end_workflow_testing__workflow_execution_success", "End-to-End Workflow Testing", "Workflow Execution Success %"),
]

@pytest.mark.parametrize('tech_slug,module_name,classification,metric', CASES)
def test_metric_module_metadata(tech_slug, module_name, classification, metric):
    mod = importlib.import_module(f"l2_fixtures.techniques.{tech_slug}.{module_name}")
    meta = mod.METRIC_META
    assert meta["l4_classification"] == classification
    assert meta["l5_metric"] == metric
    assert "primary_tool" in meta
    assert "secondary_tool" in meta
