import speech_recognition as sr
import os
import time
import playsound
from gtts import gTTS

def interviewer(text):
    tts = gTTS(text=text)
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        answer = ""
        try:
            answer = r.recognize_google(audio)
            print(answer)
        except Exception as e:
            print("Exception: " + str(e))
    return answer
