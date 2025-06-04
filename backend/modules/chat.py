import requests

def get_llm_reply(user_text: str) -> str:
    response = requests.post(
        "http://127.0.0.1:1234/v1/chat/completions",
        headers={"Content-Type": "application/json"},
        json={
            "messages": [{"role": "user", "content": user_text}],
            "model": "tinyllama-1.1b-chat-v1.0"
        }
    )
    print("Model responsed")
    return response.json()["choices"][0]["message"]["content"]

    