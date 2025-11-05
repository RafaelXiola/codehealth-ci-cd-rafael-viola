"""Simple script representing a minimal application for CI/CD demonstrations."""
from __future__ import annotations


def build_application() -> str:
    """Return a message indicating that the build step ran."""
    return "Build step executed"


def run_health_check() -> dict[str, bool]:
    """Simulate validation checks that would run in a CI pipeline."""
    return {"unit_tests": True, "style": True, "security_scan": True}


def summarize_report(checks: dict[str, bool]) -> str:
    """Generate a high-level summary for reporting in CI logs."""
    total = len(checks)
    passed = sum(1 for value in checks.values() if value)
    return f"{passed}/{total} checks passed"


def main() -> None:
    print(build_application())
    checks = run_health_check()
    print(summarize_report(checks))


if __name__ == "__main__":
    main()
