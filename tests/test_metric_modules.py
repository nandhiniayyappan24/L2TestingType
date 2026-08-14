"""Auto-generated tests ensuring every metric module loads and exposes METRIC_META."""
from __future__ import annotations
import importlib
import pytest

CASES = [
    ("accessibility_validation", "wcag_compliance_testing__wcag_compliance_score", "WCAG Compliance Testing", "WCAG Compliance Score"),
    ("cross_device_layout_validation", "breakpoint_validation__breakpoint_pass_rate", "Breakpoint Validation", "Breakpoint Pass Rate"),
    ("experience_stability", "cross_browser_testing__browser_compatibility_pass_rate", "Cross-Browser Testing", "Browser Compatibility Pass Rate"),
    ("keyboard_navigation_testing", "keyboard_accessibility_coverage__keyboard_navigation_coverage", "Keyboard Accessibility Coverage", "Keyboard Navigation Coverage"),
]

@pytest.mark.parametrize('tech_slug,module_name,classification,metric', CASES)
def test_metric_module_metadata(tech_slug, module_name, classification, metric):
    mod = importlib.import_module(f"l2_fixtures.techniques.{tech_slug}.{module_name}")
    meta = mod.METRIC_META
    assert meta["l4_classification"] == classification
    assert meta["l5_metric"] == metric
    assert "primary_tool" in meta
    assert "secondary_tool" in meta
