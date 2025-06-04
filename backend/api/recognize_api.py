from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from modules import whisper_module, chat
from utils.audio_utils import save_temp_audio

from modules.voice_detection import process_voice_text


router = APIRouter()

@router.post("/recognize")
async def recognize(file: UploadFile = File(...)):
    try:
        print("File received")
        contents = await file.read()
        if not contents:
            raise HTTPException(status_code=400, detail="Empty file uploaded")

        temp_path = save_temp_audio(contents)
        user_text = whisper_module.transcribe_audio(temp_path)
        reply_text = chat.get_llm_reply(user_text)

        await process_voice_text(user_text)

        return JSONResponse(content={"text": user_text, "reply": reply_text})

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
