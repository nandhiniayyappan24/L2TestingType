# PCI-DSS Compliance

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

**2 techniques**, **2 metrics**.

## Techniques

### Payment Data Security (`techniques/payment_data_security/`)

- **Cardholder Data Exposure Scan** → CHD Exposure Finding Count (`pylint` / `Ruff`)

### TLS/Encryption Compliance (`techniques/tlsencryption_compliance/`)

- **TLS Configuration Testing** → Weak TLS Config Count (`pylint` / `Ruff`)
