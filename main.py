import pygame
import speech_recognition as sr
import os
import time
import playsound
from gtts import gTTS
import pathlib

#Change according to person
Username = "Philip Ventura"

#Play audio file
def ai_voice():
    folder_path = ('Sound')
    count = 0
    sound_file = None  
    
    for path in pathlib.Path(folder_path).iterdir():
        if path.is_file() and path.suffix in {'.mp3', '.wav'}: 
            sound_file = str(path)
            count += 1

    print(f"Number of sound files found: {count}")
    
    if not sound_file:
        print("No sound file found in the specified directory.")
        return

    pygame.init()
    pygame.mixer.init()
    pygame.mixer_music.load(sound_file)

    while True:
        n = input("Type 'play' to play, 'stop' to pause, or 'exit' to quit: ").strip().lower()
        if n == "play":
            pygame.mixer_music.play()
        elif n == "stop":
            pygame.mixer_music.pause()
        elif n == "exit":
            pygame.mixer_music.stop()
            break  # Exit the loop
        else:
            print("Invalid input. Try again.")


def get_audio():
    print('Your turn')
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

ai_voice()
