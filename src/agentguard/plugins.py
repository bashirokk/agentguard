"""Plugin discovery through Python entry points and configured modules."""

from __future__ import annotations

import importlib
import inspect
from importlib.metadata import entry_points

from agentguard.rules.base import Rule


class PluginError(RuntimeError):
    """Raised when a configured plugin cannot be loaded safely."""


def load_plugins(modules: list[str]) -> list[Rule]:
    """Load rules from ``agentguard.rules`` entry points and module ``rules`` exports."""
    rules: list[Rule] = []
    for point in entry_points(group="agentguard.rules"):
        rules.extend(_normalize(point.load(), f"entry point {point.name}"))
    for module_name in modules:
        try:
            module = importlib.import_module(module_name)
        except Exception as exc:  # plugin failures must have actionable context
            raise PluginError(f"could not import plugin {module_name!r}: {exc}") from exc
        if not hasattr(module, "rules"):
            raise PluginError(f"plugin {module_name!r} must export `rules`")
        rules.extend(_normalize(module.rules, f"module {module_name}"))
    return rules


def _normalize(value: object, source: str) -> list[Rule]:
    if (inspect.isclass(value) and issubclass(value, Rule)) or isinstance(value, Rule):
        value = [value]
    if callable(value) and not isinstance(value, (list, tuple)):
        value = value()
    if not isinstance(value, (list, tuple)):
        raise PluginError(f"{source} must provide a rule or iterable of rules")
    result: list[Rule] = []
    for item in value:
        if inspect.isclass(item) and issubclass(item, Rule):
            item = item()
        if not isinstance(item, Rule):
            raise PluginError(f"{source} contains {item!r}, which is not a Rule")
        result.append(item)
    return result
