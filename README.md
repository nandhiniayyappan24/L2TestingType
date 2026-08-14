# Control Flow Testing

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

**3 techniques**, **22 metrics**.

## Techniques

### Branch Coverage (`techniques/branch_coverage/`)

- **Conditional Logic Testing** → Boolean Accuracy Check (`coverage.py` / `diff-cover`)
- **Control Flow Validation** → Sequence Integrity Mapping (`coverage.py` / `diff-cover`)
- **Loop Condition Testing** → Iteration Boundary Verification (`coverage.py` / `diff-cover`)
- **Edge Case Detection** → Boundary Failure Identification (`coverage.py` / `diff-cover`)
- **Logic Error Detection** → Branch Misdirection Discovery (`coverage.py` / `diff-cover`)
- **Test Case Completeness** → Decision Coverage Gap Analysis (`coverage.py` / `diff-cover`)
- **Decision Outcome Verification** → Branch Coverage % (`coverage.py` / `diff-cover`)

### Path Coverage (`techniques/path_coverage/`)

- **Path Execution Tracking** → Retrieving data. Wait a few seconds and try to cut or copy again. (`coverage.py` / `astroid`)
- **Complete Coverage Path Verification** → Full Logic Validation (`coverage.py` / `astroid`)
- **Partial Path Coverage Detection** → Gap Identification (`coverage.py` / `astroid`)
- **Nested Condition Path Testing** → Deep Logic Probing (`coverage.py` / `astroid + SlipCover`)
- **Loop Path Detection** → Iterative Route Analysis (`coverage.py` / `astroid + SlipCover`)
- **Unreachable Path Detection** → Ghost Code Discovery (`coverage.py` / `astroid + SlipCover`)
- **Exception Path Handling** → Error Flow Verification (`coverage.py` / `astroid + SlipCover`)
- **Multi-Function Path Tracking** → Cross-Component Mapping (`coverage.py` / `astroid + SlipCover`)
- **CI/CD Integration Test** → Automated Quality Enforcement (`coverage.py` / `astroid + SlipCover`)
- **Path Detection Testing** → Path Coverage % (`coverage.py` / `astroid`)

### Statement Coverage (`techniques/statement_coverage/`)

- **Unit Testing Support** → Test Case Granularity (`coverage.py` / `Ruff`)
- **Dead Code Detection** → Unreachable Logic Identification (`coverage.py` / `Ruff`)
- **Test Completeness Evaluation** → Coverage Gap Analysis (`coverage.py` / `Ruff`)
- **Basic Logic Validation** → Surface-Level Correctness (`coverage.py` / `Ruff`)
- **Code Execution Verification** → Statement Coverage % (`coverage.py` / `Ruff`)
