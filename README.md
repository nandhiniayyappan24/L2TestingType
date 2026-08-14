# Structural Analysis

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

### Cyclomatic Complexity (`techniques/cyclomatic_complexity/`)

- **Static Analysis Metric** → Execution Path Integrity (`crosshair` / `Ruff`)
- **Decision Coverage** → Decision Outcome Verification (`coverage.py` / `Ruff`)
- **Condition Coverage** → Logical Sub-expression Validation (`pymcdc` / `Ruff`)
- **Logic Coverage Metric** → Total Logical Combinatorial Coverage (`crosshair` / `Ruff`)
- **Maintainability Analysis** → Technical Debt Impact (`pylint` / `Ruff`)
- **Test Prioritization** → QA Resource Allocation (`testmon` / `Ruff`)
