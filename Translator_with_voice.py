import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
import pygame

from io import BytesIO

input_lang = "hi"
output_lang = "ja"

r=sr.Recognizer()
while True:
    def speak(text, language=output_lang):
        mp3_fo = BytesIO()
        tts = gTTS(text, lang=language)
        tts.write_to_fp(mp3_fo)
        mp3_fo.seek(0)
        sound = pygame.mixer.Sound(mp3_fo)
        sound.play()

    with sr.Microphone() as source:
        print("say something!")
        audio=r.listen(source)

        try:
            exit=r.recognize_google(audio)
            speech=r.recognize_google(audio,language=input_lang)
            if (exit=="exit application"):
                print("Thanks for using our App")
                speak("Thanks for using our App")
                break
            print(speech)
        except sr.UnknownValueError:
            print("Sorry! Cant understand your words")
            continue
        except sr.RequestError:
            print("Sorry Request failed")
            continue    

        translation=GoogleTranslator(source='auto', target=output_lang).translate(speech)
        print(translation)

        pygame.init()
        pygame.mixer.init()
        speak(translation)

  