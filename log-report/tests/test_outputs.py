"""
Verifier for dynamo/log-report.
Each test's docstring names the instruction.md success criterion it checks.
"""
import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")

# Ground truth for the fixed environment/access.log fixture.
EXPECTED_TOTAL_REQUESTS = 6
EXPECTED_UNIQUE_IPS = 3
EXPECTED_TOP_PATH = "/index.html"


def _load_report():
    assert REPORT_PATH.exists(), f"{REPORT_PATH} was not created"
    with open(REPORT_PATH) as f:
        return json.load(f)


def test_report_is_valid_json():
    """Success criterion 1: /app/report.json exists and contains valid JSON."""
    report = _load_report()
    assert isinstance(report, dict), "report.json must contain a JSON object"


def test_request_and_ip_counts():
    """Success criterion 2: total_requests and unique_ips match the log."""
    report = _load_report()
    assert report.get("total_requests") == EXPECTED_TOTAL_REQUESTS, (
        f"expected total_requests={EXPECTED_TOTAL_REQUESTS}, got {report.get('total_requests')!r}"
    )
    assert report.get("unique_ips") == EXPECTED_UNIQUE_IPS, (
        f"expected unique_ips={EXPECTED_UNIQUE_IPS}, got {report.get('unique_ips')!r}"
    )


def test_top_path():
    """Success criterion 3: top_path matches the most-requested path."""
    report = _load_report()
    assert report.get("top_path") == EXPECTED_TOP_PATH, (
        f"expected top_path={EXPECTED_TOP_PATH!r}, got {report.get('top_path')!r}"
    )