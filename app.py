

import speech_recognition as sr

import keyboard

def recognize_speech_from_mic(recognizer, microphone):
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        discordHandler(recognizer.recognize_google(audio))

    except sr.RequestError:
        print("API unavailable")

    except sr.UnknownValueError:
        print("Unable to recognize speech")

def discordHandler(phrase):
    if phrase.startswith("play"):
        newPhrase = "." + phrase
    print(newPhrase)

while True:
    try:
        if keyboard.is_pressed('½'):
            print("Activated")

            recognizer = sr.Recognizer()
            microphone = sr.Microphone()
            recognize_speech_from_mic(recognizer, microphone)
    except:
        break