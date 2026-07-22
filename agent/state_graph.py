from enum import Enum, auto
from agent.planner import choose_tool
from agent.executor import execute
from agent.reflection import reflect


class AgentStep(Enum):
    PLAN = auto()
    EXECUTE = auto()
    REFLECT = auto()
    FINISH = auto()


class StateGraph:
    def __init__(self):
        self.current_step = AgentStep.PLAN

    def transition(self, next_step: AgentStep):
        self.current_step = next_step

    def reset(self):
        self.current_step = AgentStep.PLAN

    def run(self, state):
        """
        Execute one iteration of the agent workflow.

        Currently handles planning, execution,
        and reflection.

        Final response generation remains in main.py.
        """ 

        # Plan
        self.transition(AgentStep.PLAN)

        state.plan = choose_tool(state.memory.get_messages())

        print(state.plan)

        if not state.plan["steps"]:
            state.result = "I couldn't determine an appropriate tool."
            return

        yield AgentStep.PLAN

        # Execute
        self.transition(AgentStep.EXECUTE)

        state.current_input = state.query

        for step in state.plan["steps"]:

            execution_result = execute(step, state.current_input)

            if not execution_result.success:
                current_input = execution_result.error
                break

            state.last_execution = execution_result

            state.current_input = execution_result.output

        # state.current_input = current_input

        yield AgentStep.EXECUTE

        # Reflect 
        self.transition(AgentStep.REFLECT)

        reflection_result = reflect(state.last_execution)

        print(reflection_result)

        state.last_reflection = reflection_result

        yield AgentStep.REFLECT

        # Finish 
        self.transition(AgentStep.FINISH)

        yield AgentStep.FINISH