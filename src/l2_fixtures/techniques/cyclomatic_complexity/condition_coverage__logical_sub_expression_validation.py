"""
L2 Testing Type: Structural Analysis
L3 Technique: Cyclomatic Complexity
L4 Classification: Condition Coverage
L5 Metric: Logical Sub-expression Validation
Primary Tool: pymcdc
Secondary Tool: Ruff
Module ID: structural_analysis_cyclomatic_complexity_003
"""

from __future__ import annotations

METRIC_META = {
    "l2_testing_type": "Structural Analysis",
    "l3_technique": "Cyclomatic Complexity",
    "l4_classification": "Condition Coverage",
    "l5_metric": "Logical Sub-expression Validation",
    "primary_tool": "pymcdc",
    "secondary_tool": "Ruff",
    "module_id": "structural_analysis_cyclomatic_complexity_003",
}


def compute_structural_analysis_cyclomatic_complexity_003(seed: int = 3) -> float:
    """Return a deterministic scalar representing `Logical Sub-expression Validation`."""
    value = seed * 17
    for step in range(seed % 5 + 1):
        if step % 2 == 0:
            value += step * 3
        elif step % 3 == 0:
            value -= step
        else:
            value ^= step << 1
    return float(value % 1000) / 10.0


def validate_structural_analysis_cyclomatic_complexity_003(payload: dict[str, object] | None = None) -> dict[str, object]:
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
    result["score"] = compute_structural_analysis_cyclomatic_complexity_003()
    return result


class StructuralAnalysisCyclomaticComplexity003Analyzer:
    """Technique-specific analyzer for `Condition Coverage`."""

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


def nested_logic_structural_analysis_cyclomatic_complexity_003(value: int) -> str:
    if value > 3:
        if value > 4:
            if value > 5:
                if value > 6:
                    if value > 7:
                        return 'deep-3'
                    else:
                        return 'shallow-3'

if __name__ == "__main__":
    sample = validate_structural_analysis_cyclomatic_complexity_003({"alpha": 3, "beta": "Logical Sub-expressi"})
    print(sample)
