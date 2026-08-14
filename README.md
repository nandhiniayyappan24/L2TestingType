# Dependency Analysis

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

**3 techniques**, **3 metrics**.

## Techniques

### Build Performance (`techniques/build_performance/`)

- **Build Time Regression** → Build Duration (seconds) (`pylint` / `Ruff`)

### Bundle Size Analysis (`techniques/bundle_size_analysis/`)

- **Unused Dependency Detection** → Unused Import Count (`pylint` / `Ruff`)

### Dependency Graph Analysis (`techniques/dependency_graph_analysis/`)

- **Circular Dependency Detection** → Circular Dependency Count (`pylint` / `Ruff`)
