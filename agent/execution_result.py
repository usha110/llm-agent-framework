from dataclasses import dataclass

@dataclass
class ExecutionResult:
    success: bool
    tool: str
    output: str | None = None
    error: str | None = None