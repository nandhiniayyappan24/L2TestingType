# Performance Testing

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

**4 techniques**, **8 metrics**.

## Techniques

### Endurance Testing (`techniques/endurance_testing/`)

- **Soak Testing** → Memory Leak Score (`pylint` / `Ruff`)

### Load Signal Delta (`techniques/load_signal_delta/`)

- **Load Testing** → Throughput Under Load (RPS) (`pylint` / `Ruff`)
- **Stress Testing** → Peak Load Degradation % (`pylint` / `Ruff`)
- **Baseline Comparison Testing** → Performance Regression Delta % (`pylint` / `Ruff`)
- **Concurrency Testing** → Max Concurrent Users (VU) (`pylint` / `Ruff`)

### Soak Testing (`techniques/soak_testing/`)

- **CPU Utilisation Monitoring** → Average CPU Utilisation % (Soak) (`pylint` / `Ruff`)

### Spike Testing (`techniques/spike_testing/`)

- **Traffic Surge Handling** → Spike Recovery Time (s) (`pylint` / `Ruff`)
- **Error Rate During Spike** → Spike Error Rate % (`pylint` / `Ruff`)
