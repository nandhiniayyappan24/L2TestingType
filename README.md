# Static Code Analysis

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

**3 techniques**, **18 metrics**.

## Techniques

### IaC Security Scanning (`techniques/iac_security_scanning/`)

- **Open Security Group Rule Detection** → Open Firewall Rule Count (IaC) (`pylint` / `Ruff`)
- **Unencrypted Storage Definition** → Unencrypted Storage Count (IaC) (`pylint` / `Ruff`)
- **Publicly Exposed Resource Detection** → Public Storage Bucket Count (IaC) (`pylint` / `Ruff`)
- **CIS Benchmark Compliance** → CIS Benchmark Violation Count (IaC) (`pylint` / `Ruff`)

### Lint / Rule Violations (`techniques/lint_rule_violations/`)

- **Rule Detection Test** → Violation Density per KLOC (`pylint` / `Ruff`)
- **Unused Variable Detection** → Resource Waste Identification (`pylint` / `Ruff`)
- **Naming Convention Validation** → Semantic Consistency Score (`pylint` / `Ruff`)
- **Code Style Rule Validation** → Syntactic Uniformity Score (`pylint` / `Ruff`)
- **Complexity Rule Detection** → Structural Threshold Monitoring (`pylint` / `Ruff`)
- **Rule Severity Classification** → Impact Prioritization (`pylint` / `Ruff`)
- **Multiple Violations Detection** → Aggregated Risk Assessment (`pylint` / `Ruff`)
- **False Positive Prevention** → Accuracy Tuning (`pylint` / `Ruff`)
- **Custom Rule Validation** → Project-Specific Enforcement (`pylint` / `Ruff`)
- **Configuration File Handling** → Environment Standardization (`pylint` / `Ruff`)
- **CI/CD Integration Validation** → Automated Gatekeeping (`pylint` / `Ruff`)
- **Violation Reporting Validation** → Quality Audit Trail (`pylint` / `Ruff`)

### Secret Detection (`techniques/secret_detection/`)

- **Hardcoded Secret Scan** → Secrets Exposed in Code Count (`pylint` / `Ruff`)
- **Pre-Commit Secret Prevention** → Blocked Secret Commit Count (`pylint` / `Ruff`)
