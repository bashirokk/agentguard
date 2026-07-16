# GitHub project setup

Recommended repository description:

> Open-source AI agent security scanner for secrets, prompt injection, unsafe tools, excessive privileges, system access, APIs, validation, and dependencies.

Recommended topics:

`ai-agents`, `security`, `sast`, `llm-security`, `prompt-injection`, `langchain`, `crewai`, `autogen`, `openai`, `mcp`, `python`, `devsecops`, `security-scanner`

After creating the repository:

1. Enable Issues, Discussions, private vulnerability reporting, dependency graph, Dependabot alerts, and secret scanning where available.
2. Create labels: `bug`, `security`, `rule`, `framework`, `cli`, `reporting`, `documentation`, `good first issue`, `help wanted`, and `blocked`.
3. Create the five issues in [GOOD_FIRST_ISSUES.md](GOOD_FIRST_ISSUES.md).
4. Enable Discussions categories: Announcements, Q&A, Ideas, Show and tell, and Rule proposals.
5. Pin an introductory Discussion using `.github/DISCUSSION_TEMPLATE/welcome.yml` as the guide.
6. Protect `main`: require pull requests, one approval, conversation resolution, and the `test`, `package`, and `CodeQL` checks; disallow force pushes and deletions.
7. Configure PyPI trusted publishing for the `release.yml` workflow before tagging a release.
8. Register for the OpenSSF Best Practices badge, then add the assigned project badge.
9. Add a social preview derived from `docs/assets/social-preview.svg`.

Sponsors is intentionally empty until a funding account is created. Update `.github/FUNDING.yml` then publish a sponsor prospectus describing maintenance, response, and roadmap funding goals.
