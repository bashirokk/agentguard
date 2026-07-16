"""Rule authoring primitives."""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterable
from dataclasses import dataclass

from agentguard.context import SourceFile
from agentguard.models import Finding, Location, Severity


@dataclass(frozen=True, slots=True)
class RuleMetadata:
    id: str
    title: str
    severity: Severity
    category: str
    description: str


class Rule(ABC):
    """Base class for built-in and third-party security rules."""

    metadata: RuleMetadata

    @abstractmethod
    def scan(self, source: SourceFile) -> Iterable[Finding]:
        """Return findings for a single file."""

    def finding(
        self,
        source: SourceFile,
        line: int,
        explanation: str,
        risk: str,
        remediation: str,
        *,
        column: int = 1,
        confidence: str = "high",
        references: tuple[str, ...] = (),
        metadata: dict[str, object] | None = None,
    ) -> Finding:
        return Finding(
            rule_id=self.metadata.id,
            title=self.metadata.title,
            severity=self.metadata.severity,
            location=Location(source.path, line, column),
            explanation=explanation,
            risk=risk,
            remediation=remediation,
            category=self.metadata.category,
            confidence=confidence,
            references=references,
            metadata=metadata or {},
        )
