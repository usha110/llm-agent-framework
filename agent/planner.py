import json

from llm.client import client
from prompts.planner_prompt import build_planner_prompt

def choose_tool(conversation):

    system_prompt = build_planner_prompt()

    #print("=" * 80)
    #print(system_prompt)
    #print("=" * 80)

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

    return json.loads(response.choices[0].message.content)