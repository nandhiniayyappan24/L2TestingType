# Compliance URL (API Service)

Branch for Excel sheet **Compliance URL (API Service)** from `Testable_Strategy_Metrics_Mapping_v0.2`.

Python primary tool versions reference: `Final_Enterprise_Mapping_Matrix 1.xlsx` (Python sheet).

**15 L3 techniques**, **17 L4/L5 mappings**.

## L3 Techniques

### API Endpoint Validation (`techniques/api_endpoint_validation/`)

- **Unauthenticated Endpoint Testing** → Unauthenticated API Endpoint Count (excel tool: `OWASP ZAP / 42Crunch`, python: `pylint` / `Ruff`)

### Audit Evidence Completeness (`techniques/audit_evidence_completeness/`)

- **SOC 2 Evidence Collection Rate** → Evidence Collection Rate % (excel tool: `Drata`, python: `pylint` / `Ruff`)

### Authentication & Authorization Testing (`techniques/authentication_authorization_testing/`)

- **Broken Access Control Testing** → Unauthorized Access Count (excel tool: `ZAP Attack Proxy (OWASP)`, python: `pylint` / `Ruff`)

### Authorization Testing (`techniques/authorization_testing/`)

- **BOLA / IDOR Testing** → BOLA Finding Count (excel tool: `Postman / ZAP`, python: `pylint` / `Ruff`)

### Change Management Testing (`techniques/change_management_testing/`)

- **Change Control Verification** → Unreviewed Change Count (excel tool: `GitHub (branch protection API)`, python: `pylint` / `Ruff`)

### Consent & Age-Gate Compliance (`techniques/consent_age_gate_compliance/`)

- **COPPA Age Verification Testing** → Age-Gate Bypass Count (excel tool: `Playwright`, python: `pylint` / `Ruff`)

### Cookie & Consent Testing (`techniques/cookie_consent_testing/`)

- **Cookie Consent Compliance** → Non-Consented Tracker Count (excel tool: `OneTrust Cookie Consent`, python: `pylint` / `Ruff`)

### DAST — Dynamic Application Security Testing (`techniques/dast_dynamic_application_security_testing/`)

- **OWASP Top 10 Vulnerability Scan** → OWASP High/Critical Finding Count (excel tool: `ZAP Attack Proxy (OWASP)`, python: `pylint` / `Ruff`)
- **SQL Injection Testing** → SQLi Vulnerability Count (excel tool: `ZAP Attack Proxy (OWASP)`, python: `pylint` / `Ruff`)
- **XSS Testing** → XSS Vulnerability Count (excel tool: `ZAP Attack Proxy (OWASP)`, python: `pylint` / `Ruff`)

### Data Subject Rights Testing (`techniques/data_subject_rights_testing/`)

- **Right-to-Erasure Testing** → Data Deletion Verification Rate (excel tool: `Postman`, python: `pylint` / `Ruff`)

### PII in API Responses (`techniques/pii_in_api_responses/`)

- **PII Exposure in Live Responses** → PII in API Response Count (excel tool: `Presidio + mitmproxy`, python: `pylint` / `Ruff`)

### Payment Data Security (`techniques/payment_data_security/`)

- **Cardholder Data Exposure Scan** → CHD Exposure Finding Count (excel tool: `OWASP ZAP`, python: `pylint` / `Ruff`)

### Rate Limiting Compliance (`techniques/rate_limiting_compliance/`)

- **Rate Limit Enforcement Testing** → APIs Without Rate Limiting Count (excel tool: `Postman / Newman`, python: `pylint` / `Ruff`)

### Session Management Testing (`techniques/session_management_testing/`)

- **Session Timeout Compliance** → Session Timeout Compliance Rate (excel tool: `Postman / Playwright`, python: `pylint` / `Ruff`)

### TLS/Encryption Compliance (`techniques/tlsencryption_compliance/`)

- **TLS Configuration Testing** → Weak TLS Config Count (excel tool: `testssl.sh (OSS)`, python: `pylint` / `Ruff`)

### Transport Security (`techniques/transport_security/`)

- **Security Header Validation** → Missing Security Header Count (excel tool: `OWASP ZAP`, python: `pylint` / `Ruff`)
