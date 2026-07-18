from enum import Enum, auto


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
        Execute one iteration of the workflow.

        Currently this only drives the state transitions.
        Planner/Executor/Reflection logic will be moved
        here in the next commits.
        """

        self.transition(AgentStep.PLAN)

        yield AgentStep.PLAN

        self.transition(AgentStep.EXECUTE)

        yield AgentStep.EXECUTE

        self.transition(AgentStep.REFLECT)

        yield AgentStep.REFLECT

        self.transition(AgentStep.FINISH)

        yield AgentStep.FINISH