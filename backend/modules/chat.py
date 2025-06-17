import requests

# def get_llm_reply(user_text: str) -> str:
#     payload = {
#         "model": "phi",
#         "prompt": user_text,
#         "stream": False  
#     }
#     response = requests.post("http://10.2.60.55:11434/api/generate", json=payload)
#     result = response.json()
#     print("Model responsed: ", result["response"])
#     return result["response"]

def get_llm_reply(user_text: str) -> str:

    response = requests.get("http://10.2.60.163:8000/response", params={"prompt": "{key}".format(key=user_text)})
    result = response.json()
    print("Model responsed: ", result)
    return result