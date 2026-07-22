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

    current_input = state.query

    for current_step in state.graph.run(state):

        if current_step == AgentStep.PLAN:
            continue

        elif current_step == AgentStep.EXECUTE:
            continue

        elif current_step == AgentStep.REFLECT:

            reflection_result = reflect(state.last_execution)

            print("\nReflection")
            print(f"Should Retry : {reflection_result.should_retry}")
            print(f"Reason       : {reflection_result.reason}")
            print(f"Next Action  : {reflection_result.next_action}")

            state.last_reflection = reflection_result

        elif current_step == AgentStep.FINISH:

            state.result = state.current_input

    print(f"\nAssistant: {state.result}")

    state.memory.add_assistant(state.result)
    state.scratchpad.clear()