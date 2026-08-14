# Performance Code (Repository)

Branch for Excel sheet **Performance Code (Repository)** from `Testable_Strategy_Metrics_Mapping_v0.2`.

Python primary tool versions reference: `Final_Enterprise_Mapping_Matrix 1.xlsx` (Python sheet).

**9 L3 techniques**, **10 L4/L5 mappings**.

## L3 Techniques

### Algorithmic Complexity (`techniques/algorithmic_complexity/`)

- **Complexity-Based Performance Risk** → Cyclomatic Complexity (Performance Hotspots) (excel tool: `Lizard`, python: `radon-lizard` / `Ruff`)
- **Big-O Complexity Review** → Nested Loop Depth Count (excel tool: `Radon AST / custom AST parser`, python: `pylint` / `Ruff`)

### Build Performance (`techniques/build_performance/`)

- **Build Time Regression** → Build Duration (seconds) (excel tool: `GitHub Actions / GitLab CI/CD`, python: `pylint` / `Ruff`)

### Bundle Size Analysis (`techniques/bundle_size_analysis/`)

- **Unused Dependency Detection** → Unused Import Count (excel tool: `pylint`, python: `pylint` / `Ruff`)

### Concurrency Analysis (`techniques/concurrency_analysis/`)

- **Thread-Safety Pattern Detection** → Race Condition Risk Count (excel tool: `Semgrep (concurrency rules)`, python: `pylint` / `Ruff`)

### Database Query Analysis (`techniques/database_query_analysis/`)

- **N+1 Query Pattern Detection** → N+1 Query Anti-Pattern Count (excel tool: `Semgrep / AST Analysis`, python: `pylint` / `Ruff`)

### Dependency Graph Analysis (`techniques/dependency_graph_analysis/`)

- **Circular Dependency Detection** → Circular Dependency Count (excel tool: `pylint import graph`, python: `pylint` / `Ruff`)

### Memory Management (`techniques/memory_management/`)

- **Memory Allocation Pattern Analysis** → Large Allocation in Loop Count (excel tool: `Semgrep / AST Analysis`, python: `pylint` / `Ruff`)

### Technical Debt (`techniques/technical_debt/`)

- **Code Churn in Performance-Critical Paths** → Churn Score (Performance Modules) (excel tool: `pydriller / git log`, python: `pydriller` / `Ruff`)

### Test Coverage (`techniques/test_coverage/`)

- **Performance Test Code Coverage** → Performance Test Coverage % (excel tool: `Coverage.py`, python: `coverage.py` / `Ruff`)
