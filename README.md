# Frontend Testing

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

### DOM & Interaction Validation (`techniques/dom_interaction_validation/`)

- **Element Interaction Testing** → Interaction Success Rate (`pylint` / `Ruff`)

### Visual Regression Testing (`techniques/visual_regression_testing/`)

- **Screenshot Comparison** → Visual Regression Failure Rate (`pylint` / `Ruff`)
