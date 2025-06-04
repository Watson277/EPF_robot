import whisper

model = whisper.load_model("base")

def transcribe_audio(path: str) -> str:
    result = model.transcribe(path, language="en")
    print("Text transcribed")
    return result["text"]

