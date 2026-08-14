# Compatibility Testing

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

**4 techniques**, **4 metrics**.

## Techniques

### Accessibility Validation (`techniques/accessibility_validation/`)

- **WCAG Compliance Testing** → WCAG Compliance Score (`pylint` / `Ruff`)

### Cross-Device Layout Validation (`techniques/cross_device_layout_validation/`)

- **Breakpoint Validation** → Breakpoint Pass Rate (`pylint` / `Ruff`)

### Experience Stability (`techniques/experience_stability/`)

- **Cross-Browser Testing** → Browser Compatibility Pass Rate (`pylint` / `Ruff`)

### Keyboard Navigation Testing (`techniques/keyboard_navigation_testing/`)

- **Keyboard Accessibility Coverage** → Keyboard Navigation Coverage (`pylint` / `Ruff`)
