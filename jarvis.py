
# Creating your own jarvis
#
# Installed three libraries for this
# speech Recognition, text to speech libraries and pyAudio
#
# pip install SpeechRecognition
#
# pip install pyttsx3
#
# pip install PyAudio

# to install pyAudio in your system you'll first
# need to install wheel
# pip install wheel

# pip install pywhatkit

# pip install pyjokes

# pip install wikipedia

import speech_recognition as sr

import pyttsx3

import pywhatkit

import datetime

import wikipedia

import pyjokes

# from datetime import date

# creating a new recognizer instance
listener = sr.Recognizer()

engine = pyttsx3.init()

# If you want a female voice write the next two lines
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)


def jarvis_say(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        voice = listener.listen(source=source, timeout=5)

    try:
        data = listener.recognize_google(voice)
        data = data.lower()
        if 'jarvis' in data:
            data = data.replace('jarvis', '')
        print(data)
        return data

    except sr.UnknownValueError:
        print("Error")

    except sr.RequestError:
        print("Request Error")


def service():
    command = listen()
    if 'play' in command:
        song = command.replace('play', '')
        jarvis_say('playing '+song)
        pywhatkit.playonyt(song)

    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        jarvis_say('Current time is '+time)
        print(time)

    if 'date' in command:
        today = datetime.date.today().strftime('%d %b %Y')
        jarvis_say('Today is '+today)
        print(today)

    if 'who is' in command:
        person = command.replace('who is ', '')
        info = wikipedia.summary(person, sentences=2)
        print(info)
        jarvis_say(info)

    if 'joke' in command:
        jk = pyjokes.get_jokes()
        print(jk[0])
        jarvis_say(jk[0])

    if 'info on' in command:
        inform = command.replace('info on', '')
        print(inform)
        pywhatkit.info(inform)

    if 'exit' in command:
        jarvis_say('Glad to serve you!')
        exit()


hello_msg = 'Hi Jarvis at your service!'
jarvis_say(hello_msg)

while True:
    service()
