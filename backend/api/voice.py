import requests
import pyttsx3
import speech_recognition as sr
import mouvement as mv
import json
import time

engine = pyttsx3.init()
url = 'http://10.2.60.211:8000/reponse'  # 确保 IP 和端口正确
r = sr.Recognizer()

function_map = {
    "avancer": mv.avancer,
    "reculer": mv.reculer
}

def run_speech_loop():
    while True:
        with sr.Microphone() as source:
            print("🎤 Parlez...")
            audio = r.listen(source)

            try:
                text = r.recognize_google(audio, language="fr-FR")
                print("Texte reconnu :", text)
            except sr.UnknownValueError:
                print("Impossible de comprendre l'audio.")
                continue
            except sr.RequestError as e:
                print(f"Erreur de requête : {e}")
                continue

        question = f"""
Tu es un assistant contrôlant un robot. À chaque fois qu'on te pose une question ou une commande, tu DOIS répondre avec un JSON.

- Si c'est une question (ex : "Quelle est la mission de l'EPF ?") répond grace au contexte donné et renvoie :
  {{
    "type": "answer",
    "content": "L’EPF forme des ingénieurs généralistes capables de s’adapter à de nombreux domaines..."
  }}

- Si c'est une commande (ex : "Avance de 2 mètres"), renvoie :
  {{
    "type": "function_call",
    "function": "avancer",
    "arguments": {{
      "distance": 2.0
    }}
  }}

Texte utilisateur : {text}
"""
        try:
            reponse = requests.get(url, params={"prompt": question})
            raw_json = reponse.json()
            print("🔍 JSON reçu :", raw_json)
        except Exception as e:
            print("❌ Erreur de requête ou de parsing JSON :", e)
            continue

        if isinstance(raw_json, str):
            try:
                data = json.loads(raw_json)
            except Exception as e:
                print("❌ Erreur de parsing JSON string :", e)
                continue
        else:
            data = raw_json

        if data["type"] == "function_call":
            func = data["function"]
            args = data["arguments"]
            if func in function_map:
                function_map[func](**args)
            else:
                print("❓ Fonction inconnue :", func)
        elif data["type"] == "answer":
            print("💬 Réponse :", data["content"])
            engine.say(data["content"])
            engine.runAndWait()
        else:
            print("⚠️ Réponse inattendue :", data)

        time.sleep(1)  # 避免过于频繁地录音
