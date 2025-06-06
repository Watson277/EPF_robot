import requests

def get_llm_reply(user_text: str) -> str:
    payload = {
        "model": "phi",
        "prompt": user_text,
        "stream": False  
    }
    response = requests.post("http://10.2.60.55:11434/api/generate", json=payload)
    result = response.json()
    print("Model responsed: ", result["response"])
    return result["response"]

    