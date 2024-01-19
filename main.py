import os
import sys

import pyttsx3
import speech_recognition as sr


import pathlib
import textwrap

import google.generativeai as genai

r = sr.Recognizer()
text_speech = pyttsx3.init()





with sr.Microphone() as source:
    print("Speak now...")
    audio = r.listen(source)

# Convert speech to text
try:
    text = r.recognize_google(audio)
    print(f"Text: {text}")
except sr.UnknownValueError:
    print("Sorry, I could not understand what you said.")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")

#Then initialise the library


def addnspeak():
     x = int(input("Give me the x "))
     y = int(input("Give me the y "))
     c = x + y
     text_speech.say(c)
     text_speech.runAndWait()



def to_markdown(text):
                text = text.replace('•', '  *')
                return (textwrap.indent(text, '> ', predicate=lambda _: True))

                print("Getting quries from LLM...")


#get your API key from "https://makersuite.google.com/app/apikey"

GOOGLE_API_KEY='Enter your API key here'

genai.configure(api_key=GOOGLE_API_KEY)

print("Just there...")

model = genai.GenerativeModel('gemini-pro')


response = model.generate_content(text)


print("Just there...")


print(to_markdown(response.text))

text_speech.say(to_markdown(response.text))
text_speech.runAndWait()


