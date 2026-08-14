# Performance URL (API Service)

Branch for Excel sheet **Performance URL (API Service)** from `Testable_Strategy_Metrics_Mapping_v0.2`.

Python primary tool versions reference: `Final_Enterprise_Mapping_Matrix 1.xlsx` (Python sheet).

**10 L3 techniques**, **16 L4/L5 mappings**.

## L3 Techniques

### Caching Effectiveness (`techniques/caching_effectiveness/`)

- **Cache Hit Rate Testing** → Cache Hit Rate % (excel tool: `K6 + Redis metrics`, python: `pylint` / `Ruff`)

### Connection Management (`techniques/connection_management/`)

- **Connection Pool Exhaustion Testing** → Connection Pool Saturation % (excel tool: `K6 + DB metrics`, python: `pylint` / `Ruff`)

### Endpoint Latency Profiling (`techniques/endpoint_latency_profiling/`)

- **Slowest Endpoint Detection** → Top-N Slowest Endpoints (p95 ms) (excel tool: `K6`, python: `pylint` / `Ruff`)

### Endurance Testing (`techniques/endurance_testing/`)

- **Soak Testing** → Memory Leak Score (excel tool: `K6`, python: `pylint` / `Ruff`)

### Error State Stability (`techniques/error_state_stability/`)

- **Error Rate Monitoring** → 4xx/5xx Error Rate % (excel tool: `K6`, python: `pylint` / `Ruff`)

### Latency Consistency (`techniques/latency_consistency/`)

- **p95 Latency Testing** → p95 Response Time (ms) (excel tool: `K6`, python: `pylint` / `Ruff`)
- **p99 Latency Testing** → p99 Response Time (ms) (excel tool: `K6`, python: `pylint` / `Ruff`)
- **Mean Response Time Monitoring** → Mean Response Time (ms) (excel tool: `K6`, python: `pylint` / `Ruff`)

### Load Signal Delta (`techniques/load_signal_delta/`)

- **Load Testing** → Throughput Under Load (RPS) (excel tool: `K6`, python: `pylint` / `Ruff`)
- **Stress Testing** → Peak Load Degradation % (excel tool: `K6`, python: `pylint` / `Ruff`)
- **Baseline Comparison Testing** → Performance Regression Delta % (excel tool: `K6`, python: `pylint` / `Ruff`)
- **Concurrency Testing** → Max Concurrent Users (VU) (excel tool: `K6`, python: `pylint` / `Ruff`)

### Soak Testing (`techniques/soak_testing/`)

- **CPU Utilisation Monitoring** → Average CPU Utilisation % (Soak) (excel tool: `K6 + Prometheus`, python: `pylint` / `Ruff`)

### Spike Testing (`techniques/spike_testing/`)

- **Traffic Surge Handling** → Spike Recovery Time (s) (excel tool: `K6`, python: `pylint` / `Ruff`)
- **Error Rate During Spike** → Spike Error Rate % (excel tool: `K6`, python: `pylint` / `Ruff`)

### Throughput Consistency (`techniques/throughput_consistency/`)

- **Request Success Rate** → Successful Request Rate % (excel tool: `K6`, python: `pylint` / `Ruff`)
