# Data Flow Testing

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

**2 techniques**, **16 metrics**.

## Techniques

### All Definition Coverage (`techniques/all_definition_coverage/`)

- **Variable Definition Detection** → All-Defs Coverage % (`beniget` / `Ruff`)
- **Definition-Use Mapping** → Data Path Correlation (`coverage.py` / `Ruff`)
- **Coverage Measurement** → DU-Path Validation (`beniget` / `Ruff`)
- **Uncovered Definition Detection** → Dead Data Identification (`pylint` / `Ruff`)
- **Edge Case Handling** → Null and Boundary Flow Analysis (`crosshair` / `Ruff`)
- **Reporting Validation** → Audit Trail Verification (`pydriller` / `Ruff`)

### All Uses Coverage (`techniques/all_uses_coverage/`)

- **Computational Use Detection (C-Use)** → Data Processing Validation (`coverage.py + beniget` / `Ruff`)
- **Predicate Use Detection (P-Use)** → Logic Influence Assessment (`coverage.py + beniget` / `Ruff`)
- **Definition-Use Pair Identification** → Path Correlation Mapping (`coverage.py + beniget` / `Ruff`)
- **All-Uses Coverage Verification** → Comprehensive Data Proofing (`coverage.py + beniget` / `Ruff`)
- **Partial Uses Coverage Detection** → Data Flow Gap Analysis (`coverage.py + beniget` / `Ruff`)
- **Multiple Definitions Handling** → Ambiguity Resolution (`coverage.py + beniget` / `Ruff`)
- **Cross-Function Use Detection** → Inter-procedural Tracking (`coverage.py + beniget` / `Ruff`)
- **Unreachable Use Detection** → Ghost Use Identification (`coverage.py + beniget` / `Ruff`)
- **Coverage Reporting Validation** → Data Integrity Audit (`coverage.py + beniget` / `Ruff`)
- **Variable Use Detection** → All-Uses Coverage % (`coverage.py + beniget` / `Ruff`)
