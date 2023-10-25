import subprocess
from AppOpener import open
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# set voices to 0 for a male voice
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning")
    elif hour>= 12 and hour <18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    assname = ("Modio Speak Version 1")
    speak("I am your virtual assistant")
    speak(assname)
def username():
    speak("What would you like to be called?")
    uname = takeCommand()
    speak("Welcome")
    speak(uname)

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('enter email here','enter email password')
    server.sendmail('enter email here', to, content)
    server.close()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f'User said: {query}\n')
    except Exception as e:
        print(e)
        print("Unable to recognize voice.")
        return 'None'
    return query
if __name__ == "__main__":
    clear = lambda: os.system('cls')
    clear()
    wishMe()
    username()

    while True:
        query = takeCommand().lower()

        if 'open google' in query:
            speak("Opening Google")
            webbrowser.open('google.com')

        elif 'open spotify' in query:
            speak('Opening Spotify')
            open('spotify')

        elif 'open steam' in query:
            speak('Opening Steam')
            open('Steam')

        elif 'open pycharm' in query:
            speak('Opening pyCharm')
            open('pyCharm')
        elif 'make me a password' or 'generate a password' in query:
            speak('Generating Password')

        elif 'open github' in query:
            speak("Opening Github")
            open('github')

        elif 'exit' in query:
            speak("Exitting.")
            break


