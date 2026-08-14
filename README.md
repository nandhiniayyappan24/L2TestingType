# Static Analysis

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

**4 techniques**, **5 metrics**.

## Techniques

### Algorithmic Complexity (`techniques/algorithmic_complexity/`)

- **Complexity-Based Performance Risk** → Cyclomatic Complexity (Performance Hotspots) (`pylint` / `Ruff`)
- **Big-O Complexity Review** → Nested Loop Depth Count (`pylint` / `Ruff`)

### Concurrency Analysis (`techniques/concurrency_analysis/`)

- **Thread-Safety Pattern Detection** → Race Condition Risk Count (`pylint` / `Ruff`)

### Database Query Analysis (`techniques/database_query_analysis/`)

- **N+1 Query Pattern Detection** → N+1 Query Anti-Pattern Count (`pylint` / `Ruff`)

### Memory Management (`techniques/memory_management/`)

- **Memory Allocation Pattern Analysis** → Large Allocation in Loop Count (`pylint` / `Ruff`)
