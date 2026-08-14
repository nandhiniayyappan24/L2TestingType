# Functional Testing

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

**5 techniques**, **9 metrics**.

## Techniques

### Flow Assurance Confidence (`techniques/flow_assurance_confidence/`)

- **Step Transition Testing** → State Transition Accuracy % (`pylint` / `Ruff`)

### Input Boundary Validity (`techniques/input_boundary_validity/`)

- **Minimum Boundary Testing** → Min Value Pass Rate (`pylint` / `Ruff`)
- **Maximum Boundary Testing** → Max Value Pass Rate (`pylint` / `Ruff`)
- **Just-Outside Boundary Testing** → Out-of-Range Rejection Rate (`pylint` / `Ruff`)

### Partition Class Coverage (`techniques/partition_class_coverage/`)

- **Valid Partition Testing** → Valid Class Pass Rate (`pylint` / `Ruff`)

### Transition Correctness (`techniques/transition_correctness/`)

- **Valid State Transition Testing** → Valid Transition Pass Rate (`pylint` / `Ruff`)

### User Journey Confidence (`techniques/user_journey_confidence/`)

- **Critical Path Testing** → Critical Path Success Rate (`pylint` / `Ruff`)
- **Happy Path Testing** → Happy Path Pass Rate (`pylint` / `Ruff`)
- **End-to-End Workflow Testing** → Workflow Execution Success % (`pylint` / `Ruff`)
