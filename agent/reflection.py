from agent.execution_result import ExecutionResult
from agent.reflection_result import ReflectionResult


def reflect(result: ExecutionResult) -> ReflectionResult:

    if result.success:
        return ReflectionResult(
            should_retry=False,
            reason="Execution succeeded.",
            next_action="Finish"
        )

    error = (result.error or "").lower()

    retryable_errors = [
        "timeout",
        "connection",
        "network",
        "rate limit"
    ]

    if any(err in error for err in retryable_errors):
        return ReflectionResult(
            should_retry=True,
            reason=result.error,
            next_action="Retry tool"
        )

    return ReflectionResult(
        should_retry=False,
        reason=result.error,
        next_action="Ask planner/user for a new plan"
    )