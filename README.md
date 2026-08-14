# API Performance

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

### Caching Effectiveness (`techniques/caching_effectiveness/`)

- **Cache Hit Rate Testing** → Cache Hit Rate % (`pylint` / `Ruff`)

### Connection Management (`techniques/connection_management/`)

- **Connection Pool Exhaustion Testing** → Connection Pool Saturation % (`pylint` / `Ruff`)

### Endpoint Latency Profiling (`techniques/endpoint_latency_profiling/`)

- **Slowest Endpoint Detection** → Top-N Slowest Endpoints (p95 ms) (`pylint` / `Ruff`)
