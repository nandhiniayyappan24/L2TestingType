"""Auto-generated tests ensuring every metric module loads and exposes METRIC_META."""
from __future__ import annotations
import importlib
import pytest

CASES = [
    ("all_definition_coverage", "variable_definition_detection__all_defs_coverage", "Variable Definition Detection", "All-Defs Coverage %"),
    ("all_definition_coverage", "definition_use_mapping__data_path_correlation", "Definition-Use Mapping", "Data Path Correlation"),
    ("all_definition_coverage", "coverage_measurement__du_path_validation", "Coverage Measurement", "DU-Path Validation"),
    ("all_definition_coverage", "uncovered_definition_detection__dead_data_identification", "Uncovered Definition Detection", "Dead Data Identification"),
    ("all_definition_coverage", "edge_case_handling__null_and_boundary_flow_analysis", "Edge Case Handling", "Null and Boundary Flow Analysis"),
    ("all_definition_coverage", "reporting_validation__audit_trail_verification", "Reporting Validation", "Audit Trail Verification"),
    ("all_uses_coverage", "computational_use_detection_c_use__data_processing_validation", "Computational Use Detection (C-Use)", "Data Processing Validation"),
    ("all_uses_coverage", "predicate_use_detection_p_use__logic_influence_assessment", "Predicate Use Detection (P-Use)", "Logic Influence Assessment"),
    ("all_uses_coverage", "definition_use_pair_identification__path_correlation_mapping", "Definition-Use Pair Identification", "Path Correlation Mapping"),
    ("all_uses_coverage", "all_uses_coverage_verification__comprehensive_data_proofing", "All-Uses Coverage Verification", "Comprehensive Data Proofing"),
    ("all_uses_coverage", "partial_uses_coverage_detection__data_flow_gap_analysis", "Partial Uses Coverage Detection", "Data Flow Gap Analysis"),
    ("all_uses_coverage", "multiple_definitions_handling__ambiguity_resolution", "Multiple Definitions Handling", "Ambiguity Resolution"),
    ("all_uses_coverage", "cross_function_use_detection__inter_procedural_tracking", "Cross-Function Use Detection", "Inter-procedural Tracking"),
    ("all_uses_coverage", "unreachable_use_detection__ghost_use_identification", "Unreachable Use Detection", "Ghost Use Identification"),
    ("all_uses_coverage", "coverage_reporting_validation__data_integrity_audit", "Coverage Reporting Validation", "Data Integrity Audit"),
    ("all_uses_coverage", "variable_use_detection__all_uses_coverage", "Variable Use Detection", "All-Uses Coverage %"),
]

@pytest.mark.parametrize('tech_slug,module_name,classification,metric', CASES)
def test_metric_module_metadata(tech_slug, module_name, classification, metric):
    mod = importlib.import_module(f"l2_fixtures.techniques.{tech_slug}.{module_name}")
    meta = mod.METRIC_META
    assert meta["l4_classification"] == classification
    assert meta["l5_metric"] == metric
    assert "primary_tool" in meta
    assert "secondary_tool" in meta
