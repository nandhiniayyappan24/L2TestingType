# IaC Security

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

### IaC Scanning (`techniques/iac_scanning/`)

- **Open Security Group Rule Detection** → Open Firewall Rule Count (`pylint` / `Ruff`)
- **Unencrypted Storage Definition** → Unencrypted Storage Count (`pylint` / `Ruff`)
- **Publicly Exposed Resource Detection** → Public Storage Bucket Count (`pylint` / `Ruff`)
- **CIS Benchmark Compliance** → CIS Benchmark Violation Count (`pylint` / `Ruff`)
