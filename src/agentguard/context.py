"""Per-file context made available to security rules."""

from __future__ import annotations

import ast
from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class SourceFile:
    """A decoded source file and lazy Python syntax tree."""

    path: Path
    root: Path
    content: str
    language: str
    _tree: ast.AST | None = field(default=None, init=False, repr=False)
    _parsed: bool = field(default=False, init=False, repr=False)

    @property
    def lines(self) -> list[str]:
        return self.content.splitlines()

    @property
    def relative_path(self) -> Path:
        return self.path.relative_to(self.root)

    def python_tree(self) -> ast.AST | None:
        if self.language != "python":
            return None
        if not self._parsed:
            try:
                self._tree = ast.parse(self.content, filename=str(self.path))
            except SyntaxError:
                self._tree = None
            self._parsed = True
        return self._tree
