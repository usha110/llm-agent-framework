class ConversationMemory:
    def __init__(self):
        self.messages = []

    def add_user(self, message):
        self.messages.append({
            "role": "user",
            "content": str(message)
        })

    def add_assistant(self, message):
        self.messages.append({
            "role": "assistant",
            "content": str(message)
        })

    def get_messages(self):
        return self.messages