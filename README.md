# Compliance Code (Repository)

Branch for Excel sheet **Compliance Code (Repository)** from `Testable_Strategy_Metrics_Mapping_v0.2`.

Python primary tool versions reference: `Final_Enterprise_Mapping_Matrix 1.xlsx` (Python sheet).

**6 L3 techniques**, **10 L4/L5 mappings**.

## L3 Techniques

### Change Management Testing (`techniques/change_management_testing/`)

- **Change Control Verification** → Unreviewed Change Count (excel tool: `GitHub Branch Protection API`, python: `pylint` / `Ruff`)

### IaC Security Scanning (`techniques/iac_security_scanning/`)

- **Open Security Group Rule Detection** → Open Firewall Rule Count (IaC) (excel tool: `Checkov / tfsec`, python: `pylint` / `Ruff`)
- **Unencrypted Storage Definition** → Unencrypted Storage Count (IaC) (excel tool: `Checkov / tfsec`, python: `pylint` / `Ruff`)
- **Publicly Exposed Resource Detection** → Public Storage Bucket Count (IaC) (excel tool: `Checkov / kics`, python: `pylint` / `Ruff`)
- **CIS Benchmark Compliance** → CIS Benchmark Violation Count (IaC) (excel tool: `Checkov`, python: `pylint` / `Ruff`)

### PII Logging Detection (`techniques/pii_logging_detection/`)

- **PII in Log Statements** → PII Log Statement Count (excel tool: `Semgrep (custom rules)`, python: `pylint` / `Ruff`)

### Secret Detection (`techniques/secret_detection/`)

- **Hardcoded Secret Scan** → Secrets Exposed in Code Count (excel tool: `Gitleaks / Trufflehog`, python: `pylint` / `Ruff`)
- **Pre-Commit Secret Prevention** → Blocked Secret Commit Count (excel tool: `detect-secrets / Gitleaks`, python: `pylint` / `Ruff`)

### Secret Management (`techniques/secret_management/`)

- **Secrets in Repo History** → Historical Secret Exposure Count (excel tool: `Trufflehog`, python: `pylint` / `Ruff`)

### Student PII Exposure Scan (`techniques/student_pii_exposure_scan/`)

- **PII in Codebase Detection** → PII in Codebase Count (excel tool: `Microsoft Presidio (fed files)`, python: `pylint` / `Ruff`)
