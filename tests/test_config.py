from __future__ import annotations

from pathlib import Path

import pytest

from agentguard.config import Config


def test_load_defaults(project: Path) -> None:
    config = Config.load(None, project)
    assert "node_modules/**" in config.exclude


def test_load_config(project: Path) -> None:
    path = project / ".agentguard.yml"
    path.write_text(
        "exclude: [generated/**]\ndisabled_rules: [AG010]\nseverity_overrides: {AG006: high}\n",
        encoding="utf-8",
    )
    config = Config.load(path, project)
    assert "generated/**" in config.exclude
    assert config.disabled_rules == {"AG010"}
    assert config.severity_overrides["AG006"] == "high"


@pytest.mark.parametrize(
    "content",
    ["- not-a-map", "unknown: true", "exclude: nope", "severity_overrides: []"],
)
def test_invalid_config(project: Path, content: str) -> None:
    path = project / "bad.yml"
    path.write_text(content, encoding="utf-8")
    with pytest.raises(ValueError):
        Config.load(path, project)
