"""Configuration loading and validation."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

DEFAULT_EXCLUDES = (
    ".git/**",
    ".venv/**",
    "venv/**",
    "node_modules/**",
    "dist/**",
    "build/**",
    "coverage/**",
    ".mypy_cache/**",
    ".pytest_cache/**",
    ".ruff_cache/**",
)


@dataclass(slots=True)
class Config:
    """Scanner configuration."""

    exclude: list[str] = field(default_factory=lambda: list(DEFAULT_EXCLUDES))
    disabled_rules: set[str] = field(default_factory=set)
    severity_overrides: dict[str, str] = field(default_factory=dict)
    plugin_modules: list[str] = field(default_factory=list)
    max_file_size_kb: int = 1024
    follow_symlinks: bool = False

    @classmethod
    def load(cls, path: Path | None, root: Path) -> Config:
        candidate = path or root / ".agentguard.yml"
        if not candidate.exists():
            return cls()
        raw = yaml.safe_load(candidate.read_text(encoding="utf-8")) or {}
        if not isinstance(raw, dict):
            raise ValueError(f"{candidate}: configuration must be a mapping")
        allowed = {
            "exclude",
            "disabled_rules",
            "severity_overrides",
            "plugins",
            "max_file_size_kb",
            "follow_symlinks",
        }
        unknown = set(raw) - allowed
        if unknown:
            raise ValueError(f"{candidate}: unknown keys: {', '.join(sorted(unknown))}")
        defaults = cls()
        overrides = raw.get("severity_overrides", {})
        if not isinstance(overrides, dict):
            raise ValueError("severity_overrides must be a mapping")
        return cls(
            exclude=[*defaults.exclude, *cls._strings(raw.get("exclude", []), "exclude")],
            disabled_rules=set(cls._strings(raw.get("disabled_rules", []), "disabled_rules")),
            severity_overrides={str(key): str(value) for key, value in overrides.items()},
            plugin_modules=cls._strings(raw.get("plugins", []), "plugins"),
            max_file_size_kb=int(raw.get("max_file_size_kb", 1024)),
            follow_symlinks=bool(raw.get("follow_symlinks", False)),
        )

    @staticmethod
    def _strings(value: Any, name: str) -> list[str]:
        if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
            raise ValueError(f"{name} must be a list of strings")
        return value
