# API Testing

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

**5 techniques**, **5 metrics**.

## Techniques

### Consumer-Driven Contract Testing (`techniques/consumer_driven_contract_testing/`)

- **Pact Contract Verification** → Consumer Contract Pass Rate (`pylint` / `Ruff`)

### Contract Reliability (`techniques/contract_reliability/`)

- **OpenAPI Contract Testing** → Contract Conformance Rate (`pylint` / `Ruff`)

### Interface Reliability (`techniques/interface_reliability/`)

- **API Availability Testing** → API Uptime % (`pylint` / `Ruff`)

### Response Integrity Testing (`techniques/response_integrity_testing/`)

- **Payload Accuracy Validation** → Payload Accuracy Score (`pylint` / `Ruff`)

### Schema Drift Detection (`techniques/schema_drift_detection/`)

- **Breaking Change Detection** → Schema Drift Frequency (`pylint` / `Ruff`)
