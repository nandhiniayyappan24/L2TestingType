"""Auto-generated tests ensuring every metric module loads and exposes METRIC_META."""
from __future__ import annotations
import importlib
import pytest

CASES = [
    ("endurance_testing", "soak_testing__memory_leak_score", "Soak Testing", "Memory Leak Score"),
    ("load_signal_delta", "load_testing__throughput_under_load_rps", "Load Testing", "Throughput Under Load (RPS)"),
    ("load_signal_delta", "stress_testing__peak_load_degradation", "Stress Testing", "Peak Load Degradation %"),
    ("load_signal_delta", "baseline_comparison_testing__performance_regression_delta", "Baseline Comparison Testing", "Performance Regression Delta %"),
    ("load_signal_delta", "concurrency_testing__max_concurrent_users_vu", "Concurrency Testing", "Max Concurrent Users (VU)"),
    ("soak_testing", "cpu_utilisation_monitoring__average_cpu_utilisation_soak", "CPU Utilisation Monitoring", "Average CPU Utilisation % (Soak)"),
    ("spike_testing", "traffic_surge_handling__spike_recovery_time_s", "Traffic Surge Handling", "Spike Recovery Time (s)"),
    ("spike_testing", "error_rate_during_spike__spike_error_rate", "Error Rate During Spike", "Spike Error Rate %"),
]

@pytest.mark.parametrize('tech_slug,module_name,classification,metric', CASES)
def test_metric_module_metadata(tech_slug, module_name, classification, metric):
    mod = importlib.import_module(f"l2_fixtures.techniques.{tech_slug}.{module_name}")
    meta = mod.METRIC_META
    assert meta["l4_classification"] == classification
    assert meta["l5_metric"] == metric
    assert "primary_tool" in meta
    assert "secondary_tool" in meta
