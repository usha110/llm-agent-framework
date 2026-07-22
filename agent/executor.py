from agent.execution_result import ExecutionResult
from tools.registry import TOOLS
from pydantic import ValidationError

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

    print(f"Executing: {tool_name}")

    last_error = None

    # Validate input (no retry)
    try:
        validated_input = tool.input_model(**arguments)
        print(f"Input: {validated_input.model_dump()}")
    except ValidationError as e:
        return ExecutionResult(
        success=False,
        tool=tool_name,
        error=f"Input validation failed: {e}"
        )
    
    
    for attempt in range(MAX_RETRIES):

        try:          
            output = tool.function(**validated_input.model_dump())
            validated_output = tool.output_model(result=output)

            print(f"Output: {validated_output.result}")
            
            return ExecutionResult(
                success=True,
                tool=tool_name,
                # output=validated_output.model_dump(),
                output=validated_output.result
            )

        except ValidationError as e:
            return ExecutionResult(
            success=False,
            tool=tool_name,
            error=f"Output validation failed: {e}"
            )
        
        except Exception as e:
            last_error = str(e)
            print(f"Attempt {attempt + 1} failed: {e}")

    return ExecutionResult(
        success=False,
        tool=tool_name,
        error=last_error
    )