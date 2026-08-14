# OWASP Testing

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

**2 techniques**, **5 metrics**.

## Techniques

### Authentication & Authorization Testing (`techniques/authentication_authorization_testing/`)

- **Broken Access Control Testing** → Unauthorized Access Count (`pylint` / `Ruff`)

### DAST — Dynamic Application Security Testing (`techniques/dast_dynamic_application_security_testing/`)

- **OWASP Top 10 Vulnerability Scan** → OWASP High/Critical Finding Count (`pylint` / `Ruff`)
- **SQL Injection Testing** → SQLi Vulnerability Count (`pylint` / `Ruff`)
- **XSS Testing** → XSS Vulnerability Count (`pylint` / `Ruff`)
- **Server-Side Request Forgery (SSRF) Testing** → SSRF Vulnerability Count (`pylint` / `Ruff`)
