# Security policy

## Supported versions

Security fixes are provided for the latest minor release. During the `0.x` series, users should upgrade to the newest published version before reporting a problem that may already be fixed.

## Report a vulnerability

Please use GitHub’s **Report a vulnerability** button in the Security tab of `amic25/agentguard`. Do not open a public issue and do not include real secrets, private source code, or exploit targets in a discussion.

Include, when possible:

- affected AgentGuard version and environment;
- a minimal synthetic reproduction;
- security impact and realistic attacker prerequisites;
- whether the issue affects the scanner itself or creates a false negative;
- suggested remediation or embargo constraints.

We aim to acknowledge a report within 3 business days, provide an initial assessment within 7 business days, and coordinate disclosure after a fix is available. Timelines may change based on complexity; reporters will receive status updates.

## Scope

In scope: arbitrary code execution or file access caused by scanning, secret disclosure in reports/logs, dependency or release-pipeline compromise, bypasses that systematically hide high-impact findings, and vulnerabilities in official distribution artifacts.

Out of scope: isolated heuristic false positives, missing detection for an undocumented pattern without a security-boundary bypass, social engineering, denial of service requiring intentionally enormous inputs beyond configured limits, and vulnerabilities only in unsupported versions.

AgentGuard never needs real credentials for testing. If a report accidentally contains one, revoke it immediately and tell us it was exposed.
