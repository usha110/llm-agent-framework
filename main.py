from agent.planner import choose_tool
from agent.executor import execute
from agent.execution_result import ExecutionResult
from agent.reflection import reflect
from agent.state import AgentState
from agent.state_graph import AgentStep

state = AgentState()

while True:

    state.query = input("User: ")
    print(f"DEBUG Query: {repr(state.query)}")

    if state.query.lower() in ["exit", "quit"]:
        break
    # Start a fresh workflow for this query
    state.graph.reset()

    state.memory.add_user(state.query)

    print(state.memory.get_messages())

    state.graph.transition(AgentStep.PLAN)
    print(f"\nCurrent State : {state.graph.current_step.name}")

    state.plan = choose_tool(state.memory.get_messages())

    print(state.plan)

    if not state.plan["steps"]:
        state.result = "I couldn't determine an appropriate tool for this request."
        print(f"\nAssistant: {state.result}")
        state.memory.add_assistant(state.result)
        state.scratchpad.clear()
        continue

    state.graph.transition(AgentStep.EXECUTE)
    print(f"\nCurrent State : {state.graph.current_step.name}")
    # Initial input to the first tool
    current_input = state.query

    for step in state.plan["steps"]:

        execution_result = execute(step, current_input)

        if not execution_result.success:
            break

        # Safety check
        if not isinstance(execution_result, ExecutionResult):
            print("Executor returned an invalid result.")
            break

        # Tool failed
        if not execution_result.success:
            print(f"\nTool '{execution_result.tool}' failed")
            print(f"Reason: {execution_result.error}")

            current_input = f"Error: {execution_result.error}"
            break

        # -------------------------
        # Reflection Step
        # -------------------------
        state.graph.transition(AgentStep.REFLECT)
        print(f"\nCurrent State : {state.graph.current_step.name}")
        reflection_result = reflect(execution_result)

        print("\nReflection")

        print(f"Should Retry : {reflection_result.should_retry}")
        print(f"Reason       : {reflection_result.reason}")
            
        print(f"Next Action  : {reflection_result.next_action}")

        if reflection_result.should_retry:
            print(f"Retry suggested: {reflection_result.reason}")

        #if not reflection_result.success:
            # print(reflection_result.feedback)

        state.scratchpad.add(
            execution_result.tool,
            {
                "input": current_input,
                "arguments": step.get("arguments", {}),
                "success": execution_result.success,
                "output": execution_result.output,
                "reflection": {
                    "should_retry": reflection_result.should_retry,
                    "reason": reflection_result.reason,
                    "next_action": reflection_result.next_action,
                    },
                "error": execution_result.error
            }
        )

        current_input = execution_result.output

    state.graph.transition(AgentStep.FINISH)
    print(f"\nCurrent State : {state.graph.current_step.name}")
    final_output = current_input    
    state.result = final_output

    print("\nScratchpad")
    for item in state.scratchpad.get_entries():
        print(item)

    print(f"\nAssistant: {state.result}")

    state.memory.add_assistant(state.result)
    state.scratchpad.clear()