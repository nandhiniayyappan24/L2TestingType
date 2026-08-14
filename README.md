# L2TestingType

Python metric fixture repository. **Each branch is a standalone, installable Python project** covering a specific L2 Testing Type or Excel sheet category.

## Is This a Proper Project?

**Yes — on every working branch (35 branches).** Each branch includes:

| Component | Purpose |
|-----------|---------|
| `pyproject.toml` | Installable Python package |
| `src/l2_fixtures/techniques/` | One folder per L3 Technique, one `.py` module per L4/L5 metric |
| `tests/test_metric_modules.py` | Validates every metric module loads and exposes `METRIC_META` |
| `scripts/build.py` | Build + validation pipeline |
| `Makefile` | `install`, `test`, `build` targets |
| `.github/workflows/build.yml` | CI on push/PR |
| `metrics_mapping.json` | Full L3/L4/L5 registry for that branch |

## Coverage Summary

| Source | Unique L4/L5 Mappings | Covered |
|--------|----------------------|---------|
| All Excel sheets (deduplicated) | **183** | **183** |
| White Box (14 L3 techniques) | 100 | Yes |
| Black Box | 20 | Yes |
| Security / Compliance / Performance sheet branches | 79 | Yes |

## Branch Index

### Sheet-category branches (Excel tab = branch)

| Branch | Excel Sheet | Metrics |
|--------|-------------|---------|
| `Security-Code-Repository` | Security Code (Repository) | 9 |
| `Security-URL-API-Service` | Security URL (API Service) | 17 |
| `Compliance-URL-API-Service` | Compliance URL (API Service) | 17 |
| `Performance-URL-API-Service` | Performance URL (API Service) | 16 |
| `Performance-Code-Repository` | Performance Code (Repository) | 10 |
| `Compliance-Code-Repository` | Compliance Code (Repository) | 10 |

### L2 Testing Type branches (examples)

| Branch | Metrics |
|--------|---------|
| `Code-Quality-Auditing` | 7 |
| `Structural-Analysis` | 6 |
| `Control-Flow-Testing` | 22 |
| `Security-White-box-Testing` | 15 |
| `Static-Code-Analysis` | 18 |
| … | (35 branches total) |

Run `git branch` to see all branches.

## How to Build

Each branch builds independently. **Checkout one branch, then build only that branch.**

```bash
git clone https://github.com/nandhiniayyappan24/L2TestingType.git
cd L2TestingType
git checkout Code-Quality-Auditing   # or any branch

python -m venv .venv
.venv\Scripts\activate               # Windows
# source .venv/bin/activate          # Linux/macOS

make install
make build
```

### What happens when you run `make build`

```
make install
  ├── pip install -e ".[dev]"     # install package in editable mode
  └── pip install -r requirements.txt

make test (via build dependency)
  └── pytest tests -v             # one test per metric module

python scripts/build.py
  ├── Step 1: validate_mapping    # every L4/L5 in JSON has a Python file + METRIC_META
  ├── Step 2: pytest tests -q       # all metric modules import successfully
  ├── Step 3: coverage run pytest   # measure test coverage
  ├── Step 4: ruff + pylint       # optional static checks
  └── Writes build_report.json    # pass/fail summary
```

### CI build (GitHub Actions)

On push/PR, `.github/workflows/build.yml` runs the same pipeline on Ubuntu with Python 3.11 and uploads `build_report.json` as an artifact.

## Project layout (per branch)

```
src/l2_fixtures/techniques/<technique_slug>/
├── metrics_manifest.json
├── <classification>__<metric>.py    # METRIC_META + technique-specific Python code
└── __init__.py
tests/test_metric_modules.py
scripts/build.py
metrics_mapping.json
```

## Rules

- **Python only** — all fixture code is Python
- **No branch merging** — each branch contains only its own techniques/metrics
- **One module per L4 Classification + L5 Metric pair**
