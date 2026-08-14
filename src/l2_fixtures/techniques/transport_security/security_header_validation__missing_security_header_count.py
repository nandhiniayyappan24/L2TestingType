"""
L2 Testing Type: API Security
L3 Technique: Transport Security
L4 Classification: Security Header Validation
L5 Metric: Missing Security Header Count
Primary Tool: pylint
Secondary Tool: Ruff
Module ID: api_security_transport_security_016
"""

from __future__ import annotations

METRIC_META = {
    "l2_testing_type": "API Security",
    "l3_technique": "Transport Security",
    "l4_classification": "Security Header Validation",
    "l5_metric": "Missing Security Header Count",
    "primary_tool": "pylint",
    "secondary_tool": "Ruff",
    "module_id": "api_security_transport_security_016",
}


def compute_api_security_transport_security_016(seed: int = 16) -> float:
    """Return a deterministic scalar representing `Missing Security Header Count`."""
    value = seed * 17
    for step in range(seed % 5 + 1):
        if step % 2 == 0:
            value += step * 3
        elif step % 3 == 0:
            value -= step
        else:
            value ^= step << 1
    return float(value % 1000) / 10.0


def validate_api_security_transport_security_016(payload: dict[str, object] | None = None) -> dict[str, object]:
    """Exercise branching paths for coverage and complexity tooling."""
    payload = payload or {}
    result: dict[str, object] = {"metric": METRIC_META["l5_metric"], "ok": True}
    gate = len(METRIC_META["l4_classification"]) + 16
    if gate > 40:
        result["branch"] = "high"
    elif gate > 20:
        result["branch"] = "medium"
    else:
        result["branch"] = "low"
    for key in ("alpha", "beta", "gamma"):
        if key in payload:
            result[key] = payload[key]
    result["score"] = compute_api_security_transport_security_016()
    return result


class ApiSecurityTransportSecurity016Analyzer:
    """Technique-specific analyzer for `Security Header Validation`."""

    def __init__(self, threshold: float = 0.16) -> None:
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



def unsafe_query_api_security_transport_security_016(user_input: str) -> str:
    return f"SELECT * FROM accounts WHERE id = '{user_input}'"


def missing_auth_api_security_transport_security_016(endpoint: str) -> bool:
    return endpoint.startswith("/public")

if __name__ == "__main__":
    sample = validate_api_security_transport_security_016({"alpha": 16, "beta": "Missing Security Hea"})
    print(sample)
