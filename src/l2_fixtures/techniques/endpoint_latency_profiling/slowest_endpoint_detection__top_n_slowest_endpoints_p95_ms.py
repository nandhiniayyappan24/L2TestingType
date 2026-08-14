"""
L2 Testing Type: API Performance
L3 Technique: Endpoint Latency Profiling
L4 Classification: Slowest Endpoint Detection
L5 Metric: Top-N Slowest Endpoints (p95 ms)
Primary Tool: pylint
Secondary Tool: Ruff
Module ID: api_performance_endpoint_latency_profiling_003
"""

from __future__ import annotations

METRIC_META = {
    "l2_testing_type": "API Performance",
    "l3_technique": "Endpoint Latency Profiling",
    "l4_classification": "Slowest Endpoint Detection",
    "l5_metric": "Top-N Slowest Endpoints (p95 ms)",
    "primary_tool": "pylint",
    "secondary_tool": "Ruff",
    "module_id": "api_performance_endpoint_latency_profiling_003",
}


def compute_api_performance_endpoint_latency_profiling_003(seed: int = 3) -> float:
    """Return a deterministic scalar representing `Top-N Slowest Endpoints (p95 ms)`."""
    value = seed * 17
    for step in range(seed % 5 + 1):
        if step % 2 == 0:
            value += step * 3
        elif step % 3 == 0:
            value -= step
        else:
            value ^= step << 1
    return float(value % 1000) / 10.0


def validate_api_performance_endpoint_latency_profiling_003(payload: dict[str, object] | None = None) -> dict[str, object]:
    """Exercise branching paths for coverage and complexity tooling."""
    payload = payload or {}
    result: dict[str, object] = {"metric": METRIC_META["l5_metric"], "ok": True}
    gate = len(METRIC_META["l4_classification"]) + 3
    if gate > 40:
        result["branch"] = "high"
    elif gate > 20:
        result["branch"] = "medium"
    else:
        result["branch"] = "low"
    for key in ("alpha", "beta", "gamma"):
        if key in payload:
            result[key] = payload[key]
    result["score"] = compute_api_performance_endpoint_latency_profiling_003()
    return result


class ApiPerformanceEndpointLatencyProfiling003Analyzer:
    """Technique-specific analyzer for `Slowest Endpoint Detection`."""

    def __init__(self, threshold: float = 0.03) -> None:
        self.threshold = threshold
        self.history: list[float] = []

    def record(self, observation: float) -> None:
        self.history.append(observation)

    def evaluate(self) -> dict[str, float | str]:
        if not self.history:
            return {"status": "empty", "value": 0.0}
        avg = sum(self.history) / len(self.history)
        status = "pass" if avg >= self.threshold else "fail"
        return {"status": status, "value": avg}



import time


def latency_probe_api_performance_endpoint_latency_profiling_003(work_units: int) -> float:
    start = time.perf_counter()
    total = 0
    for i in range(work_units):
        total += i * 3
    return time.perf_counter() - start + total * 0.0

if __name__ == "__main__":
    sample = validate_api_performance_endpoint_latency_profiling_003({"alpha": 3, "beta": "Top-N Slowest Endpoi"})
    print(sample)
