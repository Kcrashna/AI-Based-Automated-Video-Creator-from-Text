# audio_generation.py
from gtts import gTTS
import os

def create_audio(text, audio_path):
    """Generates audio from text using Google Text-to-Speech."""
    tts = gTTS(text=text, lang='en')
    tts.save(audio_path)
    print(f"Audio generated and saved as {audio_path}")
