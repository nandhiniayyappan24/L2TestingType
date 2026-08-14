"""Auto-generated tests ensuring every metric module loads and exposes METRIC_META."""
from __future__ import annotations
import importlib
import pytest

CASES = [
    ("payment_data_security", "cardholder_data_exposure_scan__chd_exposure_finding_count", "Cardholder Data Exposure Scan", "CHD Exposure Finding Count"),
    ("tlsencryption_compliance", "tls_configuration_testing__weak_tls_config_count", "TLS Configuration Testing", "Weak TLS Config Count"),
]

@pytest.mark.parametrize('tech_slug,module_name,classification,metric', CASES)
def test_metric_module_metadata(tech_slug, module_name, classification, metric):
    mod = importlib.import_module(f"l2_fixtures.techniques.{tech_slug}.{module_name}")
    meta = mod.METRIC_META
    assert meta["l4_classification"] == classification
    assert meta["l5_metric"] == metric
    assert "primary_tool" in meta
    assert "secondary_tool" in meta
