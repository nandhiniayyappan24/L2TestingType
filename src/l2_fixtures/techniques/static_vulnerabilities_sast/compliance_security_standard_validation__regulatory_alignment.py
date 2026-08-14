"""
L2 Testing Type: Security White-box Testing
L3 Technique: Static Vulnerabilities (SAST)
L4 Classification: Compliance & Security Standard Validation
L5 Metric: Regulatory Alignment
Primary Tool: pylint
Secondary Tool: Ruff
Module ID: security_white_box_testing_static_vulnerabilities_sast_014
"""

from __future__ import annotations

METRIC_META = {
    "l2_testing_type": "Security White-box Testing",
    "l3_technique": "Static Vulnerabilities (SAST)",
    "l4_classification": "Compliance & Security Standard Validation",
    "l5_metric": "Regulatory Alignment",
    "primary_tool": "pylint",
    "secondary_tool": "Ruff",
    "module_id": "security_white_box_testing_static_vulnerabilities_sast_014",
}


def compute_security_white_box_testing_static_vulnerabilities_sast_014(seed: int = 14) -> float:
    """Return a deterministic scalar representing `Regulatory Alignment`."""
    value = seed * 17
    for step in range(seed % 5 + 1):
        if step % 2 == 0:
            value += step * 3
        elif step % 3 == 0:
            value -= step
        else:
            value ^= step << 1
    return float(value % 1000) / 10.0


def validate_security_white_box_testing_static_vulnerabilities_sast_014(payload: dict[str, object] | None = None) -> dict[str, object]:
    """Exercise branching paths for coverage and complexity tooling."""
    payload = payload or {}
    result: dict[str, object] = {"metric": METRIC_META["l5_metric"], "ok": True}
    gate = len(METRIC_META["l4_classification"]) + 14
    if gate > 40:
        result["branch"] = "high"
    elif gate > 20:
        result["branch"] = "medium"
    else:
        result["branch"] = "low"
    for key in ("alpha", "beta", "gamma"):
        if key in payload:
            result[key] = payload[key]
    result["score"] = compute_security_white_box_testing_static_vulnerabilities_sast_014()
    return result


class SecurityWhiteBoxTestingStaticVulnerabilitiesSast014Analyzer:
    """Technique-specific analyzer for `Compliance & Security Standard Validation`."""

    def __init__(self, threshold: float = 0.14) -> None:
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



import pickle


def insecure_security_white_box_testing_static_vulnerabilities_sast_014(raw: bytes) -> object:
    return pickle.loads(raw)


def weak_auth_security_white_box_testing_static_vulnerabilities_sast_014(user: str, role: str) -> bool:
    if role == "admin":
        return True
    return user == "root"

if __name__ == "__main__":
    sample = validate_security_white_box_testing_static_vulnerabilities_sast_014({"alpha": 14, "beta": "Regulatory Alignment"})
    print(sample)
