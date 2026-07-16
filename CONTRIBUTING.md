# Contributing to AgentGuard

Thank you for helping make AI agents safer. We welcome new rules, framework support, false-positive reductions, documentation, tests, and security research.

## Before you start

- Search existing issues and discussions.
- For small fixes, open a pull request directly.
- For a new rule, CLI change, or public API change, open an issue first so we can agree on scope and rule semantics.
- Never put a real credential, private exploit target, or confidential code in a test fixture.

## Development workflow

1. Fork the repository and create a focused branch: `git switch -c feat/short-name`.
2. Create a virtual environment and run `python -m pip install -e '.[dev]'`.
3. Add or update tests. A new rule needs positive, negative, suppression, and report-location cases.
4. Run `make check`.
5. Update `CHANGELOG.md` under `[Unreleased]` when behavior changes.
6. Open a pull request using the template and link its issue.

Pull requests should be small enough to review, explain security tradeoffs, avoid unrelated formatting, and preserve stable rule IDs. Maintainers may ask for false-positive analysis or real-world examples with sensitive details removed.

## Rule design checklist

- Use a unique stable ID (`AGxxx` for built-ins; namespaced IDs for plugins).
- State the precise trust boundary and attacker capability.
- Prefer syntax-aware, high-signal checks over broad keyword matching.
- Provide an actionable remediation, not only “validate input.”
- Do not include the matched secret or sensitive source line in output.
- Add confidence and references where useful.
- Never import or execute the scanned project.

See [docs/PLUGINS.md](docs/PLUGINS.md) for the external rule API.

## Commit and review conventions

Use imperative, descriptive commits such as `Add MCP wildcard permission rule`. Pull requests are squash-merged after CI and review. At least one maintainer approval is required; security-sensitive scanner changes should receive two reviewers when the project has enough maintainers.

## Community standards

Participation is governed by [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Report vulnerabilities privately according to [SECURITY.md](SECURITY.md).
