class Scratchpad:

    def __init__(self):
        self.entries = []

    def add(self, tool, content):
        self.entries.append({
            "role": tool,
            "content": content
        })

    def get_entries(self):
        return self.entries

    def clear(self):
        self.entries.clear()