# API Security

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

**6 techniques**, **7 metrics**.

## Techniques

### API Endpoint Validation (`techniques/api_endpoint_validation/`)

- **Unauthenticated Endpoint Testing** → Unauthenticated API Endpoint Count (`pylint` / `Ruff`)

### Authorization Testing (`techniques/authorization_testing/`)

- **BOLA / IDOR Testing** → BOLA Finding Count (`pylint` / `Ruff`)

### PII in API Responses (`techniques/pii_in_api_responses/`)

- **PII Exposure in Live Responses** → PII in API Response Count (`pylint` / `Ruff`)

### Rate Limiting Compliance (`techniques/rate_limiting_compliance/`)

- **Rate Limit Enforcement Testing** → APIs Without Rate Limiting Count (`pylint` / `Ruff`)

### Session Management Testing (`techniques/session_management_testing/`)

- **Session Timeout Compliance** → Session Timeout Compliance Rate (`pylint` / `Ruff`)

### Transport Security (`techniques/transport_security/`)

- **Security Header Validation** → Missing Security Header Count (`pylint` / `Ruff`)
- **TLS Configuration Testing** → Weak TLS Config Count (`pylint` / `Ruff`)
