import requests
import pyttsx3
import speech_recognition as sr
import json
import os
import sys
import time
import dialog_state
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from control import avancer2s as mv

# Initialisation voix
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[29].id)

# Micro et reconnaissance
r = sr.Recognizer()
url = 'http://10.2.60.80:8000/reponse'  # 🔧 mets ici l'IP correcte si ce n'est pas en local

function_map = {
    "avancer": mv.avancer,
    "reculer": mv.reculer
}

def run_speech_once():
    with sr.Microphone() as source:
        print("🎤 Parlez...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="fr-FR")
        print("✅ Texte reconnu :", text)
    except sr.UnknownValueError:
        print("❌ Impossible de comprendre l'audio.")
        return
    except sr.RequestError as e:
        print(f"❌ Erreur de requête : {e}")
        return

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
        data = reponse.json()
        print("🔍 JSON reçu :", data)

    except Exception as e:
        print("❌ Erreur de requête ou de parsing JSON :", e)
        return

    if isinstance(data, str):
        try:
            data = json.loads(data)
        except Exception as e:
            print("❌ Erreur de parsing JSON string :", e)
            return

    if data["type"] == "function_call":
        func = data["function"]
        args = data["arguments"]
        if func in function_map:
            function_map[func](**args)
        else:
            print("❓ Fonction inconnue :", func)
    elif data["type"] == "answer":
        print("💬 Réponse :", data["content"])
        engine.setProperty('rate', engine.getProperty('rate') - 50)
        engine.setProperty('volume', max(0.3, engine.getProperty('volume') - 0.7))
        engine.say(data["content"])
        engine.runAndWait()
    else:
        print("⚠️ Réponse inattendue :", data)
    
    


# Appel unique
if __name__ == "__main__":
    run_speech_once()
