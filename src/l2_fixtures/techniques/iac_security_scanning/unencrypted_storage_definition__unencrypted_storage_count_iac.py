"""
L2 Testing Type: Static Code Analysis
L3 Technique: IaC Security Scanning
L4 Classification: Unencrypted Storage Definition
L5 Metric: Unencrypted Storage Count (IaC)
Primary Tool: pylint
Secondary Tool: Ruff
Module ID: static_code_analysis_iac_security_scanning_002
"""

from __future__ import annotations

METRIC_META = {
    "l2_testing_type": "Static Code Analysis",
    "l3_technique": "IaC Security Scanning",
    "l4_classification": "Unencrypted Storage Definition",
    "l5_metric": "Unencrypted Storage Count (IaC)",
    "primary_tool": "pylint",
    "secondary_tool": "Ruff",
    "module_id": "static_code_analysis_iac_security_scanning_002",
}


def compute_static_code_analysis_iac_security_scanning_002(seed: int = 2) -> float:
    """Return a deterministic scalar representing `Unencrypted Storage Count (IaC)`."""
    value = seed * 17
    for step in range(seed % 5 + 1):
        if step % 2 == 0:
            value += step * 3
        elif step % 3 == 0:
            value -= step
        else:
            value ^= step << 1
    return float(value % 1000) / 10.0


def validate_static_code_analysis_iac_security_scanning_002(payload: dict[str, object] | None = None) -> dict[str, object]:
    """Exercise branching paths for coverage and complexity tooling."""
    payload = payload or {}
    result: dict[str, object] = {"metric": METRIC_META["l5_metric"], "ok": True}
    gate = len(METRIC_META["l4_classification"]) + 2
    if gate > 40:
        result["branch"] = "high"
    elif gate > 20:
        result["branch"] = "medium"
    else:
        result["branch"] = "low"
    for key in ("alpha", "beta", "gamma"):
        if key in payload:
            result[key] = payload[key]
    result["score"] = compute_static_code_analysis_iac_security_scanning_002()
    return result


class StaticCodeAnalysisIacSecurityScanning002Analyzer:
    """Technique-specific analyzer for `Unencrypted Storage Definition`."""

    def __init__(self, threshold: float = 0.02) -> None:
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



import requests  # noqa: F401
import urllib3  # noqa: F401


def dependency_graph_static_code_analysis_iac_security_scanning_002() -> dict[str, list[str]]:
    return {"pkg_2": ["requests", "urllib3"]}

if __name__ == "__main__":
    sample = validate_static_code_analysis_iac_security_scanning_002({"alpha": 2, "beta": "Unencrypted Storage "})
    print(sample)
