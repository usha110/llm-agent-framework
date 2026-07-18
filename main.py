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


            for step in state.plan["steps"]:

                execution_result = execute(step, current_input)

                if not execution_result.success:
                    current_input = execution_result.error
                    break

                state.last_execution = execution_result

                current_input = execution_result.output

        elif current_step == AgentStep.REFLECT:

            reflection_result = reflect(state.last_execution)

            print(reflection_result)

            state.last_reflection = reflection_result

        elif current_step == AgentStep.FINISH:

            state.result = current_input