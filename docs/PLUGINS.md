# Plugin authoring

Plugins let organizations enforce agent-specific policies without forking AgentGuard. Plugins execute as trusted Python code in the scanner process.

```python
from collections.abc import Iterable

from agentguard.context import SourceFile
from agentguard.models import Finding, Severity
from agentguard.rules import Rule, RuleMetadata


class NoProductionDebugTool(Rule):
    metadata = RuleMetadata(
        id="ACME001",
        title="Production debug tool enabled",
        severity=Severity.HIGH,
        category="acme-policy",
        description="Disallows the internal debug tool in deployable agents.",
    )

    def scan(self, source: SourceFile) -> Iterable[Finding]:
        for line_number, line in enumerate(source.lines, 1):
            if "DebugProductionTool(" in line:
                yield self.finding(
                    source,
                    line_number,
                    "The internal production debug tool is registered.",
                    "The agent could access privileged production diagnostics.",
                    "Remove the tool or restrict it to an isolated development policy.",
                )


rules = [NoProductionDebugTool]
```

Load a local importable module:

```yaml
plugins:
  - acme_agentguard_rules
```

For a distributable package, declare an entry point:

```toml
[project.entry-points."agentguard.rules"]
acme = "acme_agentguard_rules:rules"
```

An entry point may expose a `Rule` instance/class, a list or tuple of rules/classes, or a zero-argument factory returning that list. Rule IDs must be globally unique. Namespace third-party IDs to avoid collisions.

Test positive and negative cases, source locations, malformed input, and suppressions. Rules must not execute or import scanned code, access the network unexpectedly, mutate source files, or include sensitive matched text in finding messages.
