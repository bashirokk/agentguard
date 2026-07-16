# Hacker News launch draft

**Title:** Show HN: AgentGuard – an open-source security scanner for AI agent code

I built AgentGuard, an offline-first static scanner for Python and JavaScript/TypeScript AI agent projects.

Agent apps join untrusted text to credentials, tools, files, networks, and real side effects. Existing secret scanners and dependency audits help, but they do not usually flag agent-specific boundaries such as untrusted retrieved content entering instructions, wildcard MCP tool grants, or a transfer/deploy tool with no approval gate.

AgentGuard ships as a Python CLI (`agentguard scan .`), supports terminal/JSON/Markdown/SARIF output, and has a plugin API for organizational rules. The initial rules cover secrets, command execution, tool permissions, prompt injection, filesystem access, outbound APIs, tool schemas, approval gates, and dependencies. It recognizes patterns across LangChain, CrewAI, AutoGen, OpenAI agent apps, and MCP.

It never executes the target project and works offline. The first release is heuristic, especially for JS/TS, so I’m most interested in examples that improve precision without turning results into noise.

Repo: https://github.com/amic25/agentguard

I’d value feedback on rule design, SARIF integration, and which agent trust boundary should be analyzed next.
