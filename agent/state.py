from dataclasses import dataclass, field

from agent.memory import ConversationMemory
from agent.scratchpad import Scratchpad
from agent.state_graph import StateGraph


@dataclass
class AgentState:
    query: str = ""
    plan: dict = field(default_factory=dict)
    result: str = ""

    memory: ConversationMemory = field(default_factory=ConversationMemory)
    scratchpad: Scratchpad = field(default_factory=Scratchpad)

    graph: StateGraph = field(default_factory=StateGraph)