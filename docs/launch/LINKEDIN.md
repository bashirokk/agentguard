# LinkedIn launch draft

AI agents do more than generate text. They hold credentials, call tools, read files, reach APIs, and increasingly create real-world side effects.

Today I’m open-sourcing **AgentGuard**, a developer-focused security scanner that catches risky agent patterns before deployment:

• leaked API keys and secrets  
• prompt-injection trust-boundary mistakes  
• unsafe tools, commands, files, and outbound requests  
• excessive privileges and missing approval gates  
• weak tool-input validation and vulnerable dependencies

Run `agentguard scan .` locally or in CI. Reports are available for humans and as JSON, Markdown, or SARIF for GitHub code scanning. AgentGuard supports Python and JavaScript/TypeScript patterns across LangChain, CrewAI, AutoGen, OpenAI agent applications, and MCP—and it is offline-first and extensible with custom rules.

This is an open-source foundation, not a claim that static analysis alone makes an agent safe. I’d love contributions from application-security engineers, agent framework users, and developers with real-world edge cases.

https://github.com/amic25/agentguard

#AISecurity #DevSecOps #OpenSource #AIAgents #LLMSecurity
