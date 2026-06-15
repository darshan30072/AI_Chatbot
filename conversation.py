import json
import os

CHAT_FILE = "chat_history.json"


class Conversation:
    def __init__(self):
        self.history = [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            }
        ]

        self.load_history()

    def add_user(self, msg):
        self.history.append({
            "role": "user",
            "content": msg
        })

    def add_ai(self, msg):
        self.history.append({
            "role": "assistant",
            "content": msg
        })

        self.save_history()

    def save_history(self):
        with open(CHAT_FILE, "w", encoding="utf-8") as f:
            json.dump(self.history, f, indent=2)

    def load_history(self):
        if os.path.exists(CHAT_FILE):
            with open(CHAT_FILE, "r", encoding="utf-8") as f:
                self.history = json.load(f)
                
    def clear_history(self):
        self.history = [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            }
        ]
        self.save_history()