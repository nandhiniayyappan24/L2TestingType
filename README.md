# Code Quality

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

**2 techniques**, **2 metrics**.

## Techniques

### Technical Debt (`techniques/technical_debt/`)

- **Code Churn in Performance-Critical Paths** → Churn Score (Performance Modules) (`pylint` / `Ruff`)

### Test Coverage (`techniques/test_coverage/`)

- **Performance Test Code Coverage** → Performance Test Coverage % (`pylint` / `Ruff`)
