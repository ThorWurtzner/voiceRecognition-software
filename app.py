

import os
import speech_recognition as sr
import keyboard
import requests

# Environment variable
from dotenv import load_dotenv
load_dotenv()
# WEBHOOK_URL = os.getenv("WEBHOOK_URL")
CHANNEL_ID = os.getenv("CHANNEL_ID")
USER_AUTH = os.getenv("USER_AUTH")

# Sending to Discord
# import discord
# client = discord.Client()
# from discord import Webhook, RequestsWebhookAdapter

def recognizeSpeechFromMic(recognizer, microphone):
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
    if phrase.startswith("play") or phrase.startswith("skip") or phrase.startswith("stop") or phrase.startswith("resume") or phrase.startswith("disconnect"):
        newPhrase = "." + phrase
        print(newPhrase)

        # webhook = Webhook.from_url(WEBHOOK_URL, adapter=RequestsWebhookAdapter())
        # webhook.send(content=newPhrase)

        payload = {
            "content": newPhrase
        }

        header = {
            "authorization": USER_AUTH
        }

        r = requests.post("https://discord.com/api/v8/channels/" + CHANNEL_ID + "/messages", data=payload, headers=header)

        # @client.event
        # async def on_message(phrase):
        #     print("Inside discord func")
        #     channel = client.get_channel("")
        #     message = await channel.send(phrase)

        # client.run("")

        # on_message(newPhrase)
        
    else:
        print("Not relevant for Discord")

while True:
    if keyboard.is_pressed('½'):
        print("Activated")

        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        recognizeSpeechFromMic(recognizer, microphone)
