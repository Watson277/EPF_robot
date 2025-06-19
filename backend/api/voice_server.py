# speech_bot.py
import requests
import pyttsx3
import speech_recognition as sr
import json
import os
import sys
import time
import variables.dialog_state as dialog_state  


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'control')))
#from control import avancer2s as mv  
from control import speech
# Initialisation voix
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[29].id)

# Micro et reconnaissance
r = sr.Recognizer()
url = 'http://10.2.60.80:8000/reponse'  

function_map = {
    #"avancer":mv.avancer,
    #"reculer":mv.reculer,
    #"gauche":mv.gauche,
    #"droite":mv.droite,
    #"presentation":speech.presentation

}

def run_speech_once():
    with sr.Microphone() as source:
        print("Parlez...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="fr-FR")
        print("✅ Texte reconnu :", text)

        dialog_state.prompt_text = text

    except sr.UnknownValueError:
        print("Impossible de comprendre l'audio.")
        return
    except sr.RequestError as e:
        print(f"Erreur de requête : {e}")
        return

    question = f"""
TTu es un assistant contrôlant un robot. À chaque fois qu'on te pose une question ou une commande, tu DOIS répondre avec un JSON.

- Si c'est une question (ex : "Quelle est la mission de l'EPF ?") répond grace au contexte donné et renvoie :
  {{
    "type": "answer",
    "content": "L’EPF forme des ingénieurs généralistes capables de s’adapter à de nombreux domaines...>"
  }}

- Si c'est une commande de direction (ex : "va a gauche !") ou (ex: "tourne a gauche"), renvoie :
  {{
    "type": "function_call",
    "function": "gauche"
  }}

  - Si c'est une commande de deplacement (ex: "avance !"), renvoie :
  {{
    "type": "function_call",
    "function": "avancer"
  }}

  - Si c'est une commande pour te présenter (ex: "Presente-toi !"), renvoie :
  {{
    "type": "function_call",
    "function": "presentation"
  }}

Texte utilisateur : {text}
"""

    try:
        reponse = requests.get(url, params={"prompt": question})
        data = reponse.json()
        print("🔍 JSON reçu :", data)

    except Exception as e:
        print("Erreur de requête ou de parsing JSON :", e)
        return

    if isinstance(data, str):
        try:
            data = json.loads(data)
        except Exception as e:
            print("Erreur de parsing JSON string :", e)
            return

    if data["type"] == "function_call":
        func = data["function"]

        dialog_state.response_text = f"🦾 Commande : {func}()"

        if func in function_map:
            function_map[func]()
        else:
            print("❓ Fonction inconnue :", func)

    elif data["type"] == "answer":
        print("Réponse :", data["content"])

        dialog_state.response_text = data["content"]

        engine.setProperty('rate', engine.getProperty('rate') - 50)
        engine.setProperty('volume', max(0.3, engine.getProperty('volume') - 0.7))
        engine.say(data["content"])
        engine.runAndWait()
    else:
        print("Réponse inattendue :", data)


# Appel unique
if __name__ == "__main__":
    run_speech_once()