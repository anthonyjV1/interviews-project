import pygame
import speech_recognition as sr
import playsound
from gtts import gTTS
import pathlib

#Play audio file
def ai_voice():
    folder_path = ('Sound')
    sound_file = None  
    pygame.init()
    pygame.mixer.init()
    start = input('Type start to start: ').strip().lower()

    if start == 'start':
        for path in pathlib.Path(folder_path).iterdir():
            if path.is_file() and path.suffix in {'.mp3', '.wav'}: 
                sound_file = str(path)
                pygame.mixer_music.load(sound_file)
                pygame.mixer_music.play()
            while True:
                n = input("Type 'start' to start, 'pause' to pause, or 'next' to move to next question: ").strip().lower()
                if n == "start":
                    pygame.mixer_music.play()
                elif n == "pause":
                    pygame.mixer_music.pause()
                elif n == "next":
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
get_audio()
