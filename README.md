# Development Process Analysis

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

**1 techniques**, **5 metrics**.

## Techniques

### Code Churn (`techniques/code_churn/`)

- **Risk-Based Testing Prioritization** → Code Churn Score (`pydriller` / `Ruff`)
- **Regression Testing Focus** → Impact-Driven Verification (`pydriller` / `Ruff`)
- **Defect Prediction** → Fault Probability Modeling (`pydriller` / `Ruff`)
- **Test Case Maintenance Identification** → Validation Suite Updates (`pydriller` / `Ruff`)
- **Change Impact Analysis** → Side Effect Mapping (`pydriller` / `Ruff`)
