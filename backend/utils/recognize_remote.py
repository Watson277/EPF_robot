import requests

def recognize_remote(file_path):
    with open(file_path, "rb") as f:
        files = {"file": ("audio.webm", f, "audio/webm")}
        response = requests.post("http://10.2.60.55:7000/whisper", files=files)
        if response.status_code == 200:
            data = response.json()
            return data["text"]
        else:
            print("Error:", response.status_code, response.text)
            return ""
