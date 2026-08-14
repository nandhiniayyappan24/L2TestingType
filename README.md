# Security White-box Testing

Clean Python project structure for L2 metric fixtures.

## Project layout

```
src/l2_fixtures/techniques/<technique_slug>/  # one folder per L3 Technique
tests/                                         # validates all metric modules
scripts/build.py                               # build + validation pipeline
metrics_mapping.json                           # L2/L3/L4/L5 registry
```

## Build

```bash
python -m venv .venv
.venv\\Scripts\\activate   # Windows
make install
make build
```

**2 techniques**, **15 metrics**.

## Techniques

### Dependency Risk (SCA) (`techniques/dependency_risk_sca/`)

- **Transitive Dependency Analysis** → Hidden Relationship Mapping (`pip-audit` / `Ruff`)
- **License Compliance Testing** → Legal Risk Validation (`pip-audit` / `Ruff`)
- **Supply Chain Security Analysis** → Trust Integrity Verification (`pip-audit` / `Ruff`)
- **Dependency Health Monitoring** → Community Vitality Tracking (`pip-audit` / `Ruff`)
- **Risk Prioritization** → Mitigation Effort Ranking (`pip-audit` / `Ruff`)
- **Continuous Dependency Monitoring** → Real-Time Alerting (`pip-audit` / `Ruff`)
- **Vulnerability Dependency Detection** → Known CVE Count (`pip-audit` / `Ruff`)
- **Outdated Dependency Detection** → Version Lag Assessment (`pip-audit` / `Ruff`)

### Static Vulnerabilities (SAST) (`techniques/static_vulnerabilities_sast/`)

- **Secure Coding Validation** → Best Practice Compliance (`pylint` / `Ruff`)
- **Input Validation Testing** → Entry Point Sanitization (`pylint` / `Ruff`)
- **Data Flow Security Analysis** → Sensitive Information Tracking (`pylint` / `Ruff`)
- **Authentication & Authorization Weakness Detection** → Access Control Verification (`pylint` / `Ruff`)
- **Dependency & Library Vulnerability Detection** → Supply Chain Security (`pylint` / `Ruff`)
- **Compliance & Security Standard Validation** → Regulatory Alignment (`pylint` / `Ruff`)
- **Security Vulnerability Detection** → Exploit Surface Identification (`pylint` / `Ruff`)
