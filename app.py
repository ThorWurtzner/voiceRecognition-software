

import os
import speech_recognition as sr
import keyboard

# Environment variable
from dotenv import load_dotenv
load_dotenv()
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# Sending to Discord
from discord import Webhook, RequestsWebhookAdapter


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
    if phrase.startswith("play") or phrase.startswith("skip") or phrase.startswith("stop") or phrase.startswith("disconnect"):
        newPhrase = "." + phrase
        print(newPhrase)

        webhook = Webhook.from_url(WEBHOOK_URL, adapter=RequestsWebhookAdapter())
        webhook.send(content=newPhrase)
        
    else:
        print("Not relevant for Discord")

while True:
    if keyboard.is_pressed('½'):
        print("Activated")

        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        recognize_speech_from_mic(recognizer, microphone)
