import json

from llm.client import client
from tools.registry import TOOLS

def build_system_prompt():

    prompt = """
You are an AI Planner.

Your job is to select the best tool.

Available tools:

"""

    for tool_name, tool_info in TOOLS.items():

        prompt += f"""
Tool: {tool_name}
Description: {tool_info.description}

"""

    prompt += """

Rules:

Return ONLY valid JSON.

Format:

{
    "steps": [
        {
            "tool": "<tool_name>",
            "arguments": {}
        }
    ]
}

If multiple tools are needed, add more objects to the steps array in execution order.

For informational or explanatory questions:
1. First use web_search to retrieve relevant information.
2. Then use summarizer to generate a concise answer.

Do not explain.
Do not answer the user.
Do not add markdown.

"""

    return prompt

def choose_tool(conversation):

    system_prompt = build_system_prompt()

    response = client.chat.completions.create(

        model="gpt-4.1-mini",

        messages=[

            {
                "role": "system",
                "content": system_prompt
            },
           *conversation
        ],

        temperature=0

    )

    #return response.choices[0].message.content.strip()
    return json.loads(response.choices[0].message.content)