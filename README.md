# Code Quality Auditing

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

### Code Duplication (`techniques/code_duplication/`)

- **Defect Propagation Risk Detection** → Multi-Point Failure Probability (`jscpd` / `symilar (pylint)`)
- **Refactoring Identification** → Redundancy Localization (`jscpd` / `symilar (pylint)`)
- **Code Quality Assessment** → Structural Cleanliness Score (`jscpd` / `symilar (pylint)`)
- **Test Maintenance Reduction** → Test Suite Streamlining (`jscpd` / `symilar (pylint)`)
- **Refactoring Opportunity Detection** → Abstraction Potential (`jscpd` / `symilar (pylint)`)
- **Risk-Based Testing Prioritization** → Regression Focus Mapping (`jscpd` / `symilar (pylint)`)
- **Maintainability Testing** → Synchronization Verification (`jscpd` / `symilar (pylint)`)
