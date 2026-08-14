"""Auto-generated tests ensuring every metric module loads and exposes METRIC_META."""
from __future__ import annotations
import importlib
import pytest

CASES = [
    ("error_state_stability", "error_rate_monitoring__4xx5xx_error_rate", "Error Rate Monitoring", "4xx/5xx Error Rate %"),
    ("latency_consistency", "p95_latency_testing__p95_response_time_ms", "p95 Latency Testing", "p95 Response Time (ms)"),
    ("latency_consistency", "p99_latency_testing__p99_response_time_ms", "p99 Latency Testing", "p99 Response Time (ms)"),
    ("latency_consistency", "mean_response_time_monitoring__mean_response_time_ms", "Mean Response Time Monitoring", "Mean Response Time (ms)"),
    ("throughput_consistency", "request_success_rate__successful_request_rate", "Request Success Rate", "Successful Request Rate %"),
]

@pytest.mark.parametrize('tech_slug,module_name,classification,metric', CASES)
def test_metric_module_metadata(tech_slug, module_name, classification, metric):
    mod = importlib.import_module(f"l2_fixtures.techniques.{tech_slug}.{module_name}")
    meta = mod.METRIC_META
    assert meta["l4_classification"] == classification
    assert meta["l5_metric"] == metric
    assert "primary_tool" in meta
    assert "secondary_tool" in meta
