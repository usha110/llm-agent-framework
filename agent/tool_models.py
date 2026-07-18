from pydantic import BaseModel, Field


# ==========================================================
# Base Models
# ==========================================================

class ToolInput(BaseModel):
    """
    Base class for all tool input models.
    """
    pass


class ToolOutput(BaseModel):
    """
    Base class for all tool output models.
    """
    success: bool = Field(
        default=True,
        description="Whether the tool executed successfully."
    )


# ==========================================================
# Calculator
# ==========================================================

class CalculatorInput(ToolInput):
    """
    Input schema for Calculator Tool.
    """
    expression: str = Field(
        ...,
        description="Arithmetic expression to evaluate."
    )


class CalculatorOutput(ToolOutput):
    """
    Output schema for Calculator Tool.
    """
    result: int | float = Field(
        ...,
        description="Result of the arithmetic calculation."
    )


# ==========================================================
# Web Search
# ==========================================================

class WebSearchInput(ToolInput):
    """
    Input schema for Web Search Tool.
    """
    query: str = Field(
        ...,
        description="Search query."
    )


class WebSearchOutput(ToolOutput):
    """
    Output schema for Web Search Tool.
    """
    result: str = Field(
        ...,
        description="Search results returned by the tool."
    )


# ==========================================================
# Summarizer
# ==========================================================

class SummarizerInput(ToolInput):
    """
    Input schema for Summarizer Tool.
    """
    text: str = Field(
        ...,
        description="Text to summarize."
    )


class SummarizerOutput(ToolOutput):
    """
    Output schema for Summarizer Tool.
    """
    result: str = Field(
        ...,
        description="Summarized text."
    )