FROM python:3.12-slim AS builder
WORKDIR /build
COPY pyproject.toml README.md LICENSE ./
COPY src ./src
RUN python -m pip install --no-cache-dir --upgrade pip build && python -m build --wheel

FROM python:3.12-slim
LABEL org.opencontainers.image.title="AgentGuard" \
      org.opencontainers.image.description="AI Agent Security Scanner" \
      org.opencontainers.image.source="https://github.com/amic25/agentguard" \
      org.opencontainers.image.licenses="Apache-2.0"
RUN useradd --create-home --uid 10001 agentguard
COPY --from=builder /build/dist/*.whl /tmp/
RUN python -m pip install --no-cache-dir /tmp/*.whl && rm /tmp/*.whl
USER agentguard
WORKDIR /workspace
ENTRYPOINT ["agentguard"]
CMD ["--help"]
