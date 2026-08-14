# SOC 2 Compliance

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

**4 techniques**, **4 metrics**.

## Techniques

### Access Control (`techniques/access_control/`)

- **Privileged Access Audit** → Overprivileged Account Count (`pylint` / `Ruff`)

### Audit Evidence Completeness (`techniques/audit_evidence_completeness/`)

- **SOC 2 Evidence Collection Rate** → Evidence Collection Rate % (`pylint` / `Ruff`)

### Change Management Testing (`techniques/change_management_testing/`)

- **Change Control Verification** → Unreviewed Change Count (`pylint` / `Ruff`)

### Secret Management (`techniques/secret_management/`)

- **Secrets in Repo History** → Historical Secret Exposure Count (`pylint` / `Ruff`)
