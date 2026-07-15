from dataclasses import dataclass
from typing import Any

@dataclass
class ExecutionResult:
    success: bool
    tool: str
    output: Any = None
    error: str | None = None