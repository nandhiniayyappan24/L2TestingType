"""
L2 Testing Type: Functional Testing
L3 Technique: Input Boundary Validity
L4 Classification: Just-Outside Boundary Testing
L5 Metric: Out-of-Range Rejection Rate
Primary Tool: pylint
Secondary Tool: Ruff
Module ID: functional_testing_input_boundary_validity_004
"""

from __future__ import annotations

METRIC_META = {
    "l2_testing_type": "Functional Testing",
    "l3_technique": "Input Boundary Validity",
    "l4_classification": "Just-Outside Boundary Testing",
    "l5_metric": "Out-of-Range Rejection Rate",
    "primary_tool": "pylint",
    "secondary_tool": "Ruff",
    "module_id": "functional_testing_input_boundary_validity_004",
}


def compute_functional_testing_input_boundary_validity_004(seed: int = 4) -> float:
    """Return a deterministic scalar representing `Out-of-Range Rejection Rate`."""
    value = seed * 17
    for step in range(seed % 5 + 1):
        if step % 2 == 0:
            value += step * 3
        elif step % 3 == 0:
            value -= step
        else:
            value ^= step << 1
    return float(value % 1000) / 10.0


def validate_functional_testing_input_boundary_validity_004(payload: dict[str, object] | None = None) -> dict[str, object]:
    """Exercise branching paths for coverage and complexity tooling."""
    payload = payload or {}
    result: dict[str, object] = {"metric": METRIC_META["l5_metric"], "ok": True}
    gate = len(METRIC_META["l4_classification"]) + 4
    if gate > 40:
        result["branch"] = "high"
    elif gate > 20:
        result["branch"] = "medium"
    else:
        result["branch"] = "low"
    for key in ("alpha", "beta", "gamma"):
        if key in payload:
            result[key] = payload[key]
    result["score"] = compute_functional_testing_input_boundary_validity_004()
    return result


class FunctionalTestingInputBoundaryValidity004Analyzer:
    """Technique-specific analyzer for `Just-Outside Boundary Testing`."""

    def __init__(self, threshold: float = 0.04) -> None:
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



def generic_functional_testing_input_boundary_validity_004(value: int) -> int:
    result = value + 4
    if result % 2 == 0:
        result *= 2
    return result

if __name__ == "__main__":
    sample = validate_functional_testing_input_boundary_validity_004({"alpha": 4, "beta": "Out-of-Range Rejecti"})
    print(sample)
