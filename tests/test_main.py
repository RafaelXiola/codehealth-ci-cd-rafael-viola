from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

import main  # noqa: E402  # pylint: disable=wrong-import-position


def test_build_application_message():
    assert main.build_application() == "Build step executed"


def test_health_checks_are_positive():
    checks = main.run_health_check()
    assert all(checks.values())


def test_report_summary():
    summary = main.summarize_report({"unit": True, "lint": False})
    assert summary == "1/2 checks passed"
