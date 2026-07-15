from dataclasses import dataclass


@dataclass
class ReflectionResult:
    should_retry: bool
    reason: str
    next_action: str