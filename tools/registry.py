from dataclasses import dataclass
from typing import Callable

from pydantic import BaseModel
from typing import Type

from tools.calculator import calculator
from tools.web_search import web_search
from tools.summarizer import summarization
from agent.tool_models import (
    ToolInput,
    ToolOutput,
    CalculatorInput,
    CalculatorOutput,
    WebSearchInput,
    WebSearchOutput,
    SummarizerInput,
    SummarizerOutput,
)

@dataclass
class Tool:
    name: str
    description: str
    function: Callable

    input_model: Type[ToolInput]
    output_model: Type[ToolOutput]

TOOLS = {
    "calculator": Tool(
        name="calculator",
        description="Perform arithmetic calculations.",
        function=calculator,
        input_model=CalculatorInput,
        output_model=CalculatorOutput,
    ),

    "web_search": Tool(
        name="web_search",
        description="Search the web.",
        function=web_search,
        input_model=WebSearchInput,
        output_model=WebSearchOutput,
    ),

    "summarizer": Tool(
        name="summarizer",
        description="Summarize text.",
        function=summarization,
        input_model=SummarizerInput,
        output_model=SummarizerOutput,
    ),
}