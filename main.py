from agent.planner import choose_tool
from agent.executor import execute
from agent.memory import ConversationMemory
from agent.scratchpad import Scratchpad

from agent.state import AgentState

state = AgentState()

#memory = ConversationMemory()
#scratchpad = Scratchpad()

while True:

    state.query = input("User: ")

    if state.query.lower() in ["exit", "quit"]:
        break

    state.memory.add_user(state.query)

    print(state.memory.get_messages())

    state.plan = choose_tool(state.memory.get_messages())

    print(state.plan)

    state.result = state.query

    for step in state.plan["steps"]:

        result_before_execution = state.result

        execution = execute(step, state.result)

        if not execution.success:
            print(f"\nTool '{execution.tool}' failed")
            print(f"Reason: {execution.error}")
            state.result = f"Error: {execution.error}"
            break   

        state.result = execution.output
        
        state.scratchpad.add(
            execution.tool,
            {
                "input": result_before_execution,
                "success": execution.success,
                "output": execution.output,
                "error": execution.error,
                "arguments": step.get("arguments", {})
            }
        )

    print("\nScratchpad")

    for item in state.scratchpad.get_entries():
        print(item)

    print(f"Assistant: {state.result}")

    state.memory.add_assistant(state.result)
    state.scratchpad.clear()