"""Auto-generated tests ensuring every metric module loads and exposes METRIC_META."""
from __future__ import annotations
import importlib
import pytest

CASES = [
    ("caching_effectiveness", "cache_hit_rate_testing__cache_hit_rate", "Cache Hit Rate Testing", "Cache Hit Rate %"),
    ("connection_management", "connection_pool_exhaustion_testing__connection_pool_saturation", "Connection Pool Exhaustion Testing", "Connection Pool Saturation %"),
    ("endpoint_latency_profiling", "slowest_endpoint_detection__top_n_slowest_endpoints_p95_ms", "Slowest Endpoint Detection", "Top-N Slowest Endpoints (p95 ms)"),
]

@pytest.mark.parametrize('tech_slug,module_name,classification,metric', CASES)
def test_metric_module_metadata(tech_slug, module_name, classification, metric):
    mod = importlib.import_module(f"l2_fixtures.techniques.{tech_slug}.{module_name}")
    meta = mod.METRIC_META
    assert meta["l4_classification"] == classification
    assert meta["l5_metric"] == metric
    assert "primary_tool" in meta
    assert "secondary_tool" in meta
