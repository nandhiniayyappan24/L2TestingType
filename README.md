# Readability / Maintainability

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

**1 techniques**, **7 metrics**.

## Techniques

### Cognitive Complexity (`techniques/cognitive_complexity/`)

- **Maintainability Evaluation** → Technical Debt Impact (`cognitive-ast` / `Ruff`)
- **Testability Analysis** → Unit Test Complexity (`cognitive-ast` / `Ruff`)
- **Risk Detection** → Defect Probability (`cognitive-ast` / `Ruff`)
- **Refactoring Guidance** → Modularization Opportunity (`cognitive-ast` / `Ruff`)
- **Code Review Support** → Reviewer Fatigue Factor (`cognitive-ast` / `Ruff`)
- **Testing Effort Prioritization** → QA Resource Allocation (`cognitive-ast` / `Ruff`)
- **Code Understandability Analysis** → Human Cognitive Load (`cognitive-ast` / `Ruff`)
