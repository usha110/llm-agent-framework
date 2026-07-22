"""
Entry point for the AI agent.

This module:
- Accepts user input.
- Initializes the agent state.
- Executes the workflow using StateGraph.
- Displays the final response.
- Updates conversation memory.
"""
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

    for current_step in state.graph.run(state):

        if current_step == AgentStep.PLAN:
            continue

        elif current_step == AgentStep.EXECUTE:
            continue

        elif current_step == AgentStep.REFLECT:
            continue
            

        elif current_step == AgentStep.FINISH:

            state.result = state.current_input

    print(f"\nAssistant: {state.result}")

    state.memory.add_assistant(state.result)
    state.scratchpad.clear()