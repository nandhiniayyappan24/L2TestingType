# Secret Detection

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

**1 techniques**, **3 metrics**.

## Techniques

### Secret Scanning (`techniques/secret_scanning/`)

- **Hardcoded Secret Detection** → Secrets Exposed in Code Count (`pylint` / `Ruff`)
- **Pre-Commit Secret Prevention** → Blocked Secret Commit Count (`pylint` / `Ruff`)
- **Secrets in Git History** → Historical Secret Exposure Count (`pylint` / `Ruff`)
