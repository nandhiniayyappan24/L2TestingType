# GDPR Compliance

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

### Consent & Age-Gate Compliance (`techniques/consent_age_gate_compliance/`)

- **COPPA Age Verification Testing** → Age-Gate Bypass Count (`pylint` / `Ruff`)

### Cookie & Consent Testing (`techniques/cookie_consent_testing/`)

- **Cookie Consent Compliance** → Non-Consented Tracker Count (`pylint` / `Ruff`)

### Data Subject Rights Testing (`techniques/data_subject_rights_testing/`)

- **Right-to-Erasure Testing** → Data Deletion Verification Rate (`pylint` / `Ruff`)

### PII in API Responses (`techniques/pii_in_api_responses/`)

- **PII Exposure in Live Responses** → PII in API Response Count (`pylint` / `Ruff`)
