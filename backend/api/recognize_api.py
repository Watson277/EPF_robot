from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from modules import whisper_module, chat
from utils.audio_utils import save_temp_audio
from utils.recognize_remote import recognize_remote

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
        print(" Path: ", temp_path)

        # user_text = whisper_module.transcribe_audio(temp_path)
        user_text = recognize_remote(temp_path)

        await process_voice_text(user_text)
        print("User text: ", user_text)
        reply_text = chat.get_llm_reply(user_text)
        print("模型回复内容：", repr(reply_text))  # Print    

        return JSONResponse(content={"text": user_text, "reply": reply_text})
        print("Response returned")

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
