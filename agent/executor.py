from agent.execution_result import ExecutionResult
from tools.registry import TOOLS

MAX_RETRIES = 3

def execute(step, input_data):

    tool_name = step["tool"]
    arguments = step.get("arguments", {})

    tool = TOOLS.get(tool_name)

    if not tool:
        return ExecutionResult(
            success=False,
            tool=tool_name,
            error="Tool not found"
        )

    # Determine the input for the tool  
    tool_input = (
        arguments.get("query")
        or arguments.get("expression")
        or arguments.get("text")
        or input_data
    )

    if tool_input is None:
        tool_input = input_data

    print(f"Executing: {tool_name}")
    print(f"Input: {tool_input}")

    last_error = None

    for attempt in range(MAX_RETRIES):

        try:
            output  = tool.function(tool_input)
            #output = tool.function(arguments or {"input": input_data})

            print(f"Output: {output }")
            
            return ExecutionResult(
                success=True,
                tool=tool_name,
                output=output
            )

        except Exception as e:
            last_error = str(e)
            print(f"Attempt {attempt + 1} failed: {e}")

    return ExecutionResult(
        success=False,
        tool=tool_name,
        error=last_error
    )