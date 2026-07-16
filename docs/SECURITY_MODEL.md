# Security model

## Assets and trust boundaries

Agent applications commonly hold model/API credentials, user data, retrieved documents, system prompts, tools, and authority to create side effects. AgentGuard focuses on transitions where attacker-influenced text or tool output crosses into instructions, code, files, networks, credentials, or high-impact actions.

## Threats covered

- credentials committed in source or configuration;
- prompt injection through untrusted user, web, document, message, or tool content;
- arbitrary command/code execution exposed to model output;
- broad tool, filesystem, network, and delegation permissions;
- SSRF and plaintext outbound requests;
- weak or missing tool argument schemas;
- irreversible actions without a bound human approval;
- known vulnerable and unreproducible dependencies.

The security properties AgentGuard encourages are least privilege, explicit trust boundaries, strict validation, data/instruction separation, deny-by-default outbound access, sandboxed system access, approval for consequential actions, auditable side effects, and reproducible dependencies.

## Scanner threat model

The scanned repository is untrusted. AgentGuard reads supported UTF-8 files but does not import, build, install, or execute them. It skips symlinks and caps file size by default. Reporters do not print matched source lines or secret values. Explicit Python plugin modules are trusted code and execute in the AgentGuard process; only enable plugins from trusted packages.

## Limitations

Static, local heuristics cannot see runtime IAM policies, dynamic prompt construction, generated code, encrypted secrets, indirect data flow, external MCP server behavior, or controls enforced in infrastructure. JavaScript/TypeScript checks in the first release are lexical rather than full-AST analysis. The bundled advisory list is intentionally small and is not a replacement for `pip-audit`, `npm audit`, OSV-Scanner, or an SBOM service.

A clean result is not a certification. Teams should also threat-model agent workflows; sandbox tools; scope credentials; log and review tool calls; test adversarial prompts; scan secrets and dependencies with dedicated tools; and monitor runtime behavior.

## Severity model

| Severity | Meaning |
|---|---|
| Critical | likely direct credential compromise or arbitrary code/command execution |
| High | strong path to high-impact abuse, data access, or broad privilege misuse |
| Medium | exploitable with additional conditions or materially weak trust-boundary control |
| Low | hardening or supply-chain reproducibility gap |

Confidence is separate from severity. A high-severity, medium-confidence finding deserves investigation even when more context is required.
