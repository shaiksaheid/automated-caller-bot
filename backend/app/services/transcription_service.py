import os

os.environ["PATH"] += os.pathsep + r"C:\Program Files\ffmpeg\bin"

import requests
import whisper
from requests.auth import HTTPBasicAuth

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

model = whisper.load_model("medium")

def transcribe_audio(recording_url: str, call_sid: str) -> str | None:
    try:
        os.makedirs("temp", exist_ok=True)

        audio_path = f"temp/{call_sid}.mp3"

        # Download audio with Twilio auth
        r = requests.get(
            recording_url,
            auth=(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN")),
            timeout=30
        )
        r.raise_for_status()

        with open(audio_path, "wb") as f:
            f.write(r.content)

        result = model.transcribe(audio_path)
        text = result.get("text", "").strip()

        return text if text else None

    except Exception as e:
        print("Transcription error:", e)
        return None