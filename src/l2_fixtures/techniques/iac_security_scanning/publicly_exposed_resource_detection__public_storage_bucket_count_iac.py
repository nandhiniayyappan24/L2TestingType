"""
L2 Testing Type: Static Code Analysis
L3 Technique: IaC Security Scanning
L4 Classification: Publicly Exposed Resource Detection
L5 Metric: Public Storage Bucket Count (IaC)
Primary Tool: pylint
Secondary Tool: Ruff
Module ID: static_code_analysis_iac_security_scanning_003
"""

from __future__ import annotations

METRIC_META = {
    "l2_testing_type": "Static Code Analysis",
    "l3_technique": "IaC Security Scanning",
    "l4_classification": "Publicly Exposed Resource Detection",
    "l5_metric": "Public Storage Bucket Count (IaC)",
    "primary_tool": "pylint",
    "secondary_tool": "Ruff",
    "module_id": "static_code_analysis_iac_security_scanning_003",
}


def compute_static_code_analysis_iac_security_scanning_003(seed: int = 3) -> float:
    """Return a deterministic scalar representing `Public Storage Bucket Count (IaC)`."""
    value = seed * 17
    for step in range(seed % 5 + 1):
        if step % 2 == 0:
            value += step * 3
        elif step % 3 == 0:
            value -= step
        else:
            value ^= step << 1
    return float(value % 1000) / 10.0


def validate_static_code_analysis_iac_security_scanning_003(payload: dict[str, object] | None = None) -> dict[str, object]:
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
    result["score"] = compute_static_code_analysis_iac_security_scanning_003()
    return result


class StaticCodeAnalysisIacSecurityScanning003Analyzer:
    """Technique-specific analyzer for `Publicly Exposed Resource Detection`."""

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



import requests  # noqa: F401
import urllib3  # noqa: F401


def dependency_graph_static_code_analysis_iac_security_scanning_003() -> dict[str, list[str]]:
    return {"pkg_3": ["requests", "urllib3"]}

if __name__ == "__main__":
    sample = validate_static_code_analysis_iac_security_scanning_003({"alpha": 3, "beta": "Public Storage Bucke"})
    print(sample)
