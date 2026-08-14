#!/usr/bin/env python3
"""Build pipeline for L2 metric fixture branches."""

from __future__ import annotations

import importlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAPPING = ROOT / "metrics_mapping.json"
REPORT = ROOT / "build_report.json"


def run(cmd: list[str]) -> dict:
    proc = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    return {
        "command": " ".join(cmd),
        "returncode": proc.returncode,
        "stdout": proc.stdout[-4000:],
        "stderr": proc.stderr[-4000:],
    }


def validate_mapping() -> list[str]:
    errors: list[str] = []
    data = json.loads(MAPPING.read_text(encoding="utf-8"))
    for technique, metrics in data["techniques"].items():
        if not metrics:
            continue
        tech_slug = metrics[0].get("technique_slug") or technique
        tech_dir = ROOT / "src" / "l2_fixtures" / "techniques" / tech_slug
        manifest = tech_dir / "metrics_manifest.json"
        if not manifest.exists():
            errors.append(f"Missing manifest: {manifest}")
            continue
        entries = json.loads(manifest.read_text(encoding="utf-8"))
        for entry in entries:
            module_file = entry["module"]
            module_path = tech_dir / module_file
            if not module_path.exists():
                errors.append(f"Missing module: {module_path}")
                continue
            mod_name = f"l2_fixtures.techniques.{tech_slug}.{module_file.replace('.py', '')}"
            mod = importlib.import_module(mod_name)
            if not hasattr(mod, "METRIC_META"):
                errors.append(f"Missing METRIC_META in {mod_name}")
    return errors


def main() -> int:
    report: dict = {"steps": [], "status": "unknown"}
    errors = validate_mapping()
    report["mapping_errors"] = errors
    report["steps"].append({"name": "validate_mapping", "ok": not errors})

    pytest_step = run([sys.executable, "-m", "pytest", "tests", "-q"])
    report["steps"].append({"name": "pytest", "ok": pytest_step["returncode"] == 0, **pytest_step})

    cov_step = run([
        sys.executable, "-m", "coverage", "run", "-m", "pytest", "tests", "-q",
    ])
    report["steps"].append({"name": "coverage", "ok": cov_step["returncode"] == 0, **cov_step})

    optional_tools = []
    for tool_cmd in (
        [sys.executable, "-m", "ruff", "check", "src", "tests"],
        [sys.executable, "-m", "pylint", "src/l2_fixtures", "--disable=all", "--enable=E,F"],
    ):
        step = run(tool_cmd)
        optional_tools.append(step)
    report["optional_tool_steps"] = optional_tools

    report["status"] = "pass" if not errors and pytest_step["returncode"] == 0 else "fail"
    REPORT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps({"status": report["status"], "errors": len(errors)}, indent=2))
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
