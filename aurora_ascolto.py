import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr

DURATA = 4  # secondi

print("🎤 AuroraBot è in ascolto...")

# Registrazione audio
frequenza = 44100
audio = sd.rec(int(DURATA * frequenza), samplerate=frequenza, channels=1, dtype='int16')
sd.wait()
wav.write("comando.wav", frequenza, audio)

# Riconoscimento vocale
riconoscitore = sr.Recognizer()
with sr.AudioFile("comando.wav") as source:
    audio_data = riconoscitore.record(source)

try:
    comando = riconoscitore.recognize_google(audio_data, language="it-IT")
    print(f"🤖 Hai detto: {comando}")
except sr.UnknownValueError:
    print("❌ Non ho capito, puoi ripetere?")
except sr.RequestError as e:
    print(f"⚠️ Errore nella richiesta: {e}")
