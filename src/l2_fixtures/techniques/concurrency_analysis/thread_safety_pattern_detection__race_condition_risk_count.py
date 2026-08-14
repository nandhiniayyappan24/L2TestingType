"""
L2 Testing Type: Static Analysis
L3 Technique: Concurrency Analysis
L4 Classification: Thread-Safety Pattern Detection
L5 Metric: Race Condition Risk Count
Primary Tool: pylint
Secondary Tool: Ruff
Module ID: static_analysis_concurrency_analysis_003
"""

from __future__ import annotations

METRIC_META = {
    "l2_testing_type": "Static Analysis",
    "l3_technique": "Concurrency Analysis",
    "l4_classification": "Thread-Safety Pattern Detection",
    "l5_metric": "Race Condition Risk Count",
    "primary_tool": "pylint",
    "secondary_tool": "Ruff",
    "module_id": "static_analysis_concurrency_analysis_003",
}


def compute_static_analysis_concurrency_analysis_003(seed: int = 3) -> float:
    """Return a deterministic scalar representing `Race Condition Risk Count`."""
    value = seed * 17
    for step in range(seed % 5 + 1):
        if step % 2 == 0:
            value += step * 3
        elif step % 3 == 0:
            value -= step
        else:
            value ^= step << 1
    return float(value % 1000) / 10.0


def validate_static_analysis_concurrency_analysis_003(payload: dict[str, object] | None = None) -> dict[str, object]:
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
    result["score"] = compute_static_analysis_concurrency_analysis_003()
    return result


class StaticAnalysisConcurrencyAnalysis003Analyzer:
    """Technique-specific analyzer for `Thread-Safety Pattern Detection`."""

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



def generic_static_analysis_concurrency_analysis_003(value: int) -> int:
    result = value + 3
    if result % 2 == 0:
        result *= 2
    return result

if __name__ == "__main__":
    sample = validate_static_analysis_concurrency_analysis_003({"alpha": 3, "beta": "Race Condition Risk "})
    print(sample)
