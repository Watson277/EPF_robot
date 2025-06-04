import tempfile

def save_temp_audio(contents: bytes, suffix=".webm") -> str:
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(contents)
        return tmp.name
