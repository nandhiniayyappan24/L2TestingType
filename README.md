# Reliability Testing

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

**3 techniques**, **5 metrics**.

## Techniques

### Error State Stability (`techniques/error_state_stability/`)

- **Error Rate Monitoring** → 4xx/5xx Error Rate % (`pylint` / `Ruff`)

### Latency Consistency (`techniques/latency_consistency/`)

- **p95 Latency Testing** → p95 Response Time (ms) (`pylint` / `Ruff`)
- **p99 Latency Testing** → p99 Response Time (ms) (`pylint` / `Ruff`)
- **Mean Response Time Monitoring** → Mean Response Time (ms) (`pylint` / `Ruff`)

### Throughput Consistency (`techniques/throughput_consistency/`)

- **Request Success Rate** → Successful Request Rate % (`pylint` / `Ruff`)
