#Copyright (c) 2020, Marinos Papadakis
#All rights reserved.
#This source code is licensed under the MIT License found in the LICENSE file in the root directory of this source tree.

import itertools
import time
import playsound
from gtts import gTTS
import speech_recognition as sr
import os

# Function to record voice
def speechrec():
    z = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = z.listen(source)
            v = z.recognize_google(audio)
            vi = str(v)
            vz = vi.lower()
            print(f"Response: {vi}")
            return vz.split()
        except sr.UnknownValueError:
            return "restart"
        except sr.RequestError as e:
            return "restart"

# Function for TTS
def speak(text):
    tts = gTTS(text = text, lang='en')
    filename = "tmp/voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
