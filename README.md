# Security Code (Repository)

Branch for Excel sheet **Security Code (Repository)** from `Testable_Strategy_Metrics_Mapping_v0.2`.

Python primary tool versions reference: `Final_Enterprise_Mapping_Matrix 1.xlsx` (Python sheet).

**4 L3 techniques**, **9 L4/L5 mappings**.

## L3 Techniques

### Access Control (`techniques/access_control/`)

- **Privileged Access Audit** → Overprivileged Account Count (excel tool: `GitHub API / GitLab API`, python: `pylint` / `Ruff`)

### Change Management Testing (`techniques/change_management_testing/`)

- **Change Control Verification** → Unreviewed Change Count (excel tool: `GitHub Branch Protection API`, python: `pylint` / `Ruff`)

### IaC Scanning (`techniques/iac_scanning/`)

- **Open Security Group Rule Detection** → Open Firewall Rule Count (excel tool: `Checkov / tfsec`, python: `pylint` / `Ruff`)
- **Unencrypted Storage Definition** → Unencrypted Storage Count (excel tool: `Checkov / tfsec`, python: `pylint` / `Ruff`)
- **Publicly Exposed Resource Detection** → Public Storage Bucket Count (excel tool: `Checkov / kics`, python: `pylint` / `Ruff`)
- **CIS Benchmark Compliance** → CIS Benchmark Violation Count (excel tool: `Checkov`, python: `pylint` / `Ruff`)

### Secret Scanning (`techniques/secret_scanning/`)

- **Hardcoded Secret Detection** → Secrets Exposed in Code Count (excel tool: `Gitleaks`, python: `pylint` / `Ruff`)
- **Pre-Commit Secret Prevention** → Blocked Secret Commit Count (excel tool: `detect-secrets`, python: `pylint` / `Ruff`)
- **Secrets in Git History** → Historical Secret Exposure Count (excel tool: `Trufflehog`, python: `pylint` / `Ruff`)
