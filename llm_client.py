import requests

OLLAMA_URL = "http://localhost:11434/api/chat"


def stream_reply(history, model):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": model,
            "messages": history,
            "stream": True
        },
        stream=True
    )

    for line in response.iter_lines():
        if line:
            try:
                import json

                data = json.loads(line)

                if "message" in data:
                    yield data["message"]["content"]

            except Exception:
                pass