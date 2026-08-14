# Mutation Testing

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

**1 techniques**, **4 metrics**.

## Techniques

### Mutation Score (`techniques/mutation_score/`)

- **Fault Detection Capability** → Logic Error Sensitivity (`cosmic-ray` / `mutmut`)
- **Test Coverage Quality Validation** → Test Rigor Assessment (`cosmic-ray` / `mutmut`)
- **Test Case Improvement Identification** → Weak Spot Localization (`cosmic-ray` / `mutmut`)
- **Edge Case Detection** → Boundary Mutant Analysis (`cosmic-ray` / `mutmut`)
