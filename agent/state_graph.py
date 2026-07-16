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