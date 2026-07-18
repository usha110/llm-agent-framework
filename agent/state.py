from typing import Optional
from dataclasses import dataclass, field

from agent.memory import ConversationMemory
from agent.scratchpad import Scratchpad
from agent.state_graph import StateGraph

from agent.execution_result import ExecutionResult
from agent.reflection_result import ReflectionResult

last_execution: Optional[ExecutionResult] = None
last_reflection: Optional[ReflectionResult] = None


@dataclass
class AgentState:
    query: str = ""
    plan: dict = field(default_factory=dict)
    result: str = ""
    last_execution = None
    last_reflection = None

    memory: ConversationMemory = field(default_factory=ConversationMemory)
    scratchpad: Scratchpad = field(default_factory=Scratchpad)

    graph: StateGraph = field(default_factory=StateGraph)