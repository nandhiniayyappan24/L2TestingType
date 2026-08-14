"""Auto-generated tests ensuring every metric module loads and exposes METRIC_META."""
from __future__ import annotations
import importlib
import pytest

CASES = [
    ("branch_coverage", "conditional_logic_testing__boolean_accuracy_check", "Conditional Logic Testing", "Boolean Accuracy Check"),
    ("branch_coverage", "control_flow_validation__sequence_integrity_mapping", "Control Flow Validation", "Sequence Integrity Mapping"),
    ("branch_coverage", "loop_condition_testing__iteration_boundary_verification", "Loop Condition Testing", "Iteration Boundary Verification"),
    ("branch_coverage", "edge_case_detection__boundary_failure_identification", "Edge Case Detection", "Boundary Failure Identification"),
    ("branch_coverage", "logic_error_detection__branch_misdirection_discovery", "Logic Error Detection", "Branch Misdirection Discovery"),
    ("branch_coverage", "test_case_completeness__decision_coverage_gap_analysis", "Test Case Completeness", "Decision Coverage Gap Analysis"),
    ("branch_coverage", "decision_outcome_verification__branch_coverage", "Decision Outcome Verification", "Branch Coverage %"),
    ("path_coverage", "path_execution_tracking__retrieving_data_wait_a_few_seconds_and_try_to_cut_or_copy_again", "Path Execution Tracking", "Retrieving data. Wait a few seconds and try to cut or copy again."),
    ("path_coverage", "complete_coverage_path_verification__full_logic_validation", "Complete Coverage Path Verification", "Full Logic Validation"),
    ("path_coverage", "partial_path_coverage_detection__gap_identification", "Partial Path Coverage Detection", "Gap Identification"),
    ("path_coverage", "nested_condition_path_testing__deep_logic_probing", "Nested Condition Path Testing", "Deep Logic Probing"),
    ("path_coverage", "loop_path_detection__iterative_route_analysis", "Loop Path Detection", "Iterative Route Analysis"),
    ("path_coverage", "unreachable_path_detection__ghost_code_discovery", "Unreachable Path Detection", "Ghost Code Discovery"),
    ("path_coverage", "exception_path_handling__error_flow_verification", "Exception Path Handling", "Error Flow Verification"),
    ("path_coverage", "multi_function_path_tracking__cross_component_mapping", "Multi-Function Path Tracking", "Cross-Component Mapping"),
    ("path_coverage", "cicd_integration_test__automated_quality_enforcement", "CI/CD Integration Test", "Automated Quality Enforcement"),
    ("path_coverage", "path_detection_testing__path_coverage", "Path Detection Testing", "Path Coverage %"),
    ("statement_coverage", "unit_testing_support__test_case_granularity", "Unit Testing Support", "Test Case Granularity"),
    ("statement_coverage", "dead_code_detection__unreachable_logic_identification", "Dead Code Detection", "Unreachable Logic Identification"),
    ("statement_coverage", "test_completeness_evaluation__coverage_gap_analysis", "Test Completeness Evaluation", "Coverage Gap Analysis"),
    ("statement_coverage", "basic_logic_validation__surface_level_correctness", "Basic Logic Validation", "Surface-Level Correctness"),
    ("statement_coverage", "code_execution_verification__statement_coverage", "Code Execution Verification", "Statement Coverage %"),
]

@pytest.mark.parametrize('tech_slug,module_name,classification,metric', CASES)
def test_metric_module_metadata(tech_slug, module_name, classification, metric):
    mod = importlib.import_module(f"l2_fixtures.techniques.{tech_slug}.{module_name}")
    meta = mod.METRIC_META
    assert meta["l4_classification"] == classification
    assert meta["l5_metric"] == metric
    assert "primary_tool" in meta
    assert "secondary_tool" in meta
