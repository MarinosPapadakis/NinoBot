#Copyright (c) 2020, Marinos Papadakis
#All rights reserved.
#This source code is licensed under the MIT License found in the LICENSE file in the root directory of this source tree.

import time
from speak import speak, speechrec

# Bot's Variables
year = time.strftime("%Y")
bot_age = 2020 - int(year)
botname = "Nino"

# User's Variables
name = None
age = None

# Function to respond
def response(text):
    print(text)
    speak(text)
	
# Responses
def greeting():
    text = "Hello to you too!"
    response(text)

def typeage():
    global age
    global bot_age
    if age:
        if int(age) > int(bot_age):
            text = f"You are {age - bot_age} years older than me!"
            response(text)
        elif int(age) < int(bot_age):
            text = f"I am {bot_age - age} years older than you!"
            response(text)
        else:
            text = "We have exactly the same age!"
            response(text)
    else:
        noresponse()

def typename():
    global name
    text = f"Nice name, {name}"
    response(text)

def noresponse():
    text = "I'm not quite sure how to respond to that."
    response(text)

def tellusername():
    global name
    if name != None:
        text = f"Your name is {name}."
        response(text)
    else:
        text = "I am not quite sure."
        response(text)

def tellage():
    global age
    if age != None:
        text = f"You are {age} years old."
        response(text)
    else:
        text = "I am not quite sure."
        response(text)

def howareyou():
    text = "I'm fine! Thanks for asking, how are you?"
    response(text)

def nicetohear():
    text = "Nice to hear!"
    response(text)

def whereareyoufrom():
    text = "I am a computer bot, I live in your computer's memory."
    response(text)

def whyisthat():
    text = "Oh no, why is that?"
    response(text)
	
def restart():
    text = "Sorry, I couldn't quite get that."
    response(text)
	
def sorry():
    text = "It's okay, no need to worry about it."
    response(text)

def doyoulikeme():
    text = "Of course I like you, why wouldn't I?"
    response(text)
	
def tellaboutyourself():
    global botname
    text = f"My name is {botname}, I am a computer bot developed by Marinos Papadakis and my purpose in life is to help you as much as I can."
    response(text)
	
def howoldareyou():
    global bot_age
    text = f"I am {bot_age} years old, I was created in 2020"
    response(text)
	
def okay():
    text = "Yes"
    response(text)
	
def capital(capital, country):
    if capital == "n/a":
        text = f"{country} has no capital"
    else:
        text = f"The capital of {country} is {capital}."
    response(text)
	
def thanks():
    text = "You are welcome!"
    response(text)

def squareroot(n, sqrt):
    text = f"The square root of {n} is {sqrt}"
    response(text)

def powerof(num1, num2, result):
    text = f"{num1} raised to the power of {num2} equals {result}"
    response(text)

def domath(input, result):
    text = f"{input} equals {result}"
    response(text)

def bye():
    text = "Goodbye!"
    response(text)
    exit()