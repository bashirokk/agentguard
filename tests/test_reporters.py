from __future__ import annotations

import json
from pathlib import Path

from rich.console import Console

from agentguard.reporters import render_terminal, to_json, to_markdown, to_sarif
from agentguard.scanner import Scanner


def _result(project: Path):  # type: ignore[no-untyped-def]
    (project / "agent.py").write_text("os.system(user_input)", encoding="utf-8")
    return Scanner().scan(project)


def test_json_report(project: Path) -> None:
    payload = json.loads(to_json(_result(project)))
    assert payload["findings"][0]["rule_id"] == "AG002"
    assert payload["scan"]["counts"]["Critical"] == 1


def test_markdown_report(project: Path) -> None:
    report = to_markdown(_result(project))
    assert "# AgentGuard Security Report" in report
    assert "agent.py:1:1" in report
    assert "**Remediation:**" in report


def test_sarif_report(project: Path) -> None:
    payload = json.loads(to_sarif(_result(project)))
    assert payload["version"] == "2.1.0"
    assert payload["runs"][0]["results"][0]["ruleId"] == "AG002"


def test_terminal_report(project: Path) -> None:
    console = Console(record=True, width=120)
    render_terminal(_result(project), console)
    assert "Unsafe command execution" in console.export_text()
