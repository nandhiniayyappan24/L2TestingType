# Test Regression/Coverage Analysis

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

**1 techniques**, **6 metrics**.

## Techniques

### Coverage Delta (`techniques/coverage_delta/`)

- **Regression Testing Monitoring** → Coverage Delta % (`coverage.py` / `Ruff`)
- **Test Suite Effectiveness Tracking** → Discovery Power Assessment (`coverage.py` / `Ruff`)
- **CI/CD Quality Gate Enforcement** → Deployment Readiness Guard (`coverage.py` / `Ruff`)
- **Change Impact Analysis** → Ripple Effect Mapping (`coverage.py` / `Ruff`)
- **New Code Testing Validation** → Fresh Logic Proofing (`coverage.py` / `Ruff`)
- **Quality Improvement Measurement** → Structural Health Benchmarking (`coverage.py` / `Ruff`)
