import requests
import pyttsx3
import speech_recognition as sr
import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from control import avancer2s as mv

from control import speech

tts_engine = pyttsx3.init()
voices = tts_engine.getProperty('voices')
for index, voice in enumerate(voices):
    tts_engine.setProperty('voice', voices[29].id)




url = 'http://10.2.60.80' \
':8000/reponse'
microphone = sr.Microphone()
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Parlez...")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="fr-FR")
        print("Texte reconnu :", text)
    except sr.UnknownValueError:
        print("Impossible de comprendre l'audio.")
    except sr.RequestError as e:
        print(f"Erreur de requête : {e}")

function_map={
    "avancer":mv.avancer,
    "reculer":mv.reculer,
    "gauche":mv.gauche,
    "droite":mv.droite,
    "presentation":speech.presentation
}

question = f"""
Tu es un assistant contrôlant un robot. À chaque fois qu'on te pose une question ou une commande, tu DOIS répondre avec un JSON.

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

reponse = requests.get(url,params={"prompt" : question})
print(reponse.json())


raw_json = reponse.json()  
print("🔍 JSON reçu :", raw_json)

if isinstance(raw_json, str):
    try:
        data = json.loads(raw_json)
    except Exception as e:
        print("Erreur de parsing JSON :", e)
        exit()
else:
    data = raw_json  

if data["type"] == "function_call":
    func = data["function"]
    if func in function_map:
        function_map[func]()
    else:
        print(" Fonction inconnue :", func)
elif data["type"] == "answer":
    print(" Réponse :", data["content"])
    rate =tts_engine.getPron_speech_once()('rate')
    tts_engine.setProperty('rate',rate-50)
    volume =tts_engine.getProperty('volume')
    tts_engine.setProperty('volume',volume-0.70)
    tts_engine.say(data["content"])
    tts_engine.runAndWait()
else:
    print(" Réponse inattendue :", data)

