

import speech_recognition as sr

def recognize_speech_from_mic(recognizer, microphone):
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print(recognizer.recognize_google(audio))

    except sr.RequestError:
        print("API unavailable")

    except sr.UnknownValueError:
        print("Unable to recognize speech")

# placeholder for discord use
if True:
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    recognize_speech_from_mic(recognizer, microphone)