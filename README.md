# FERPA/COPPA Compliance

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

**3 techniques**, **4 metrics**.

## Techniques

### Consent & Age-Gate Compliance (`techniques/consent_age_gate_compliance/`)

- **COPPA Age Verification Testing** → Age-Gate Bypass Count (`pylint` / `Ruff`)

### PII Logging Detection (`techniques/pii_logging_detection/`)

- **PII in Log Statements** → PII Log Statement Count (`pylint` / `Ruff`)

### Student PII Exposure Scan (`techniques/student_pii_exposure_scan/`)

- **PII Data Exposure Detection** → PII Exposure Finding Count (`pylint` / `Ruff`)
- **PII in Codebase Detection** → PII in Codebase Count (`pylint` / `Ruff`)
