from dataclasses import dataclass
from typing import Callable
from tools.calculator import calculator
from tools.web_search import web_search
from tools.summarizer import summarization

@dataclass
class Tool:
    name: str
    description: str
    function: Callable

TOOLS = {
    "calculator": Tool(
        name="calculator",
        description="Perform arithmetic calculations.",
        function=calculator
    ),  
    "web_search": Tool(
        name="web_search",
        description="Search the web for current information.",
        function=web_search
    ),
    "summarizer": Tool(
        name="summarizer",
        description="Summarize long text.",
        #function=summarizer
        function=summarization
    ),
}