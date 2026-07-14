from llm.client import client

def summarization(text : str) -> str:

    """
    Summerizes the given text while preserving information.
    """
    prompt = f"""
    Summerize the following content.
    
    Text:
    {text}
    """ 

    response = client.chat.completions.create(
        model = "gpt-4.1-mini",
        messages =[
            {
                "role" : "system",
                "content" : (
                    "You are an expert summerizer. "
                    "Preserve all important information and remove repetation"
                    "be consise and, use bullet point"  )
            },
            {
                "role" : "user", 
                "content" : prompt
            }
        ],
        temperature = 0.2
    )
    return response.choices[0].message.content
    
