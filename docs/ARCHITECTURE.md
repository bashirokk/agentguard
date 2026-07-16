# Architecture

AgentGuard is a small, deterministic pipeline designed for safe local and CI execution.

1. The CLI validates arguments and merges defaults with `.agentguard.yml`.
2. Discovery walks only supported text files, excludes dependency/build directories, refuses symlinks by default, and caps file size.
3. `SourceFile` normalizes path, content, language, lines, and a lazily parsed Python AST.
4. Built-in rules and plugin rules inspect one file at a time and emit immutable `Finding` objects.
5. The scanner applies suppressions and severity overrides, then sorts findings deterministically.
6. Reporters serialize the same result to terminal, JSON, Markdown, or SARIF.

## Package boundaries

| Module | Responsibility |
|---|---|
| `config.py` | configuration schema and safe defaults |
| `context.py` | decoded source representation and lazy syntax trees |
| `scanner.py` | file discovery, orchestration, suppression, error isolation |
| `rules/` | built-in rule implementations and public rule base class |
| `plugins.py` | entry-point and explicit-module discovery |
| `models.py` | stable finding, location, severity, and result models |
| `reporters.py` | human and machine report serialization |
| `cli.py` | command interface and exit-code contract |

## Design decisions

- **Never execute target code.** Imports are limited to explicitly configured AgentGuard plugins.
- **Offline by default.** Results do not change because a remote service is unavailable.
- **One normalized finding model.** Every output format contains the same core evidence and remediation.
- **Per-rule error isolation.** A plugin defect becomes a scan warning rather than hiding all other results.
- **Stable IDs.** CI suppressions and SARIF history remain meaningful across releases.
- **Conservative file access.** Symlinks are skipped and very large files are bounded unless the user opts in.

## Extending the system

External packages register one rule, a list of rules, or a factory under the `agentguard.rules` entry-point group. Local organizational rules may be named under `plugins` in configuration. See [PLUGINS.md](PLUGINS.md).
