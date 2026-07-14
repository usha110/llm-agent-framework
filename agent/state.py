from agent.memory import ConversationMemory
from agent.scratchpad import Scratchpad


class AgentState:

    def __init__(self):

        self.query = ""

        self.plan = None

        self.result = None

        self.memory = ConversationMemory()

        self.scratchpad = Scratchpad()