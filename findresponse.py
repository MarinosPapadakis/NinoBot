#Copyright (c) 2020, Marinos Papadakis
#All rights reserved.
#This source code is licensed under the MIT License found in the LICENSE file in the root directory of this source tree.

#from responses import *
import responses
from helpers import findnumber, is_number, findword
import csv
import sqlite3
import webbrowser
import math
from simpleeval import simple_eval

# Function to find appropriate response
def findresponse(ui):
    if "hello" in ui or "hi" in ui or "hey" in ui or "yo" in ui:
        responses.greeting()
    elif "years" in ui and "old" and "i" in ui or "years" in ui and "old" and "i'm" in ui or "age" in ui and "my" in ui and "is" in ui:
        responses.age = findnumber(ui)
        responses.typeage()
    elif "capital" in ui and "of" in ui:
        connection = sqlite3.connect("db/country-capitals.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM countrycapitals")
        results = cursor.fetchall()
        connui = ' '.join(ui)
        for r in results:
            if str(r[0]) in str(connui):
                responses.capital(r[1], r[0])
                break
        cursor.close()
        connection.close()
    elif "what's" in ui and "my" in ui and "name" in ui or "what" in ui and "my" in ui and "name" in ui:
        responses.tellusername()
    elif "my" in ui and "name" in ui or "my" in ui and "name's" in ui:
        word = findword("is", ui)
        if not word:
            word = findword("name's", ui)
        try:
            responses.name = ui[word+1]
            responses.typename()
        except:
            responses.noresponse()
    elif "what" in ui and "age" in ui and "my" not in ui or "what's" in ui and "age" in ui and "my" not in ui or "how" in ui and "old" in ui and "are" in ui and "you" in ui:
        responses.howoldareyou()
    elif "how" in ui and "old" in ui and "am" in ui and "i" in ui or "what" in ui and "age" in ui or "whats" in ui and "age" in ui or "what's" in ui and "age" in ui:
        responses.tellage()
    elif "your" in ui and "name" in ui or "tell" in ui and "about" in ui and "you" in ui or "tell" in ui and "about" in ui and "yourself" in ui:
        responses.tellaboutyourself()
    elif "how" in ui and "are" in ui and "you" in ui:
        responses.howareyou()
    elif "not" in ui and "good" in ui:
        responses.whyisthat()
    elif "bad" in ui:
        responses.whyisthat()
    elif "good" in ui or "fine" in ui:
        responses.nicetohear()
    elif "where" in ui and "are" in ui and "from" in ui:
        responses.whereareyoufrom()
    elif ui == "restart":
        responses.restart()
    elif "sorry" in ui:
        responses.sorry()
    elif "you" in ui and "like" in ui and "me" in ui:
        responses.doyoulikeme()
    elif "okay" in ui:
        responses.okay()
    elif "thanks" in ui or "thank" in ui and "you" in ui:
        responses.thanks()
    elif "open" in ui:
        for i in range(0, len(ui)):
            word = findword("open", ui)
        url = f'http://{ui[word+1]}'
        webbrowser.get(using=None).open_new_tab(url)
    elif "google" in ui:
        word = findword("google", ui)
        connui = ' '.join(ui[(word+1):len(ui)])
        url = f'https://www.google.com/search?q={connui}'
        webbrowser.get(using=None).open_new_tab(url)
    elif "wiki" in ui:
        word = findword("wiki", ui)
        connui = ' '.join(ui[(word+1):len(ui)])
        url = f'https://en.wikipedia.org/wiki/{connui}'
        webbrowser.get(using=None).open_new_tab(url)
    elif "youtube" in ui:
        word = findword("youtube", ui)
        connui = ' '.join(ui[(word+1):len(ui)])
        url = f'https://www.youtube.com/results?search_query={connui}'
        webbrowser.get(using=None).open_new_tab(url)
    elif "+" in ui or "-" in ui or "*" in ui or "/" in ui:
        operators = ["+", "-", "/", "*"]
        r = []
        for i in range(0, len(ui)):
            if ui[i] not in operators:
                if not is_number(ui[i]):
                    ui[i] = ui[i].replace(ui[i], "")
            if ui[i] != "":
                r.append(ui[i])
        str_r = ''.join(r)
        try:
            result = str(simple_eval(str_r))
            responses.domath(str_r, result)
        except:
            responses.noresponse()
    elif "square" in ui and "root" in ui or "√" in ui:
        n = findnumber(ui)
        if n:
            sqrt = math.sqrt(n)
            responses.squareroot(n, sqrt)
        else:
            responses.noresponse()
    elif "raised" in ui and "to" in ui and "power" in ui:
        n = findword("raised", ui)
        i = findword("of", ui)
        try:
            if (n-1) >= 0:
                num1 = ui[n-1]
            else:
                num1 = None
            num2 = ui[i+1]
            num1 = int(num1)
            num2 = int(num2)
            result = pow(num1, num2)
            responses.powerof(num1, num2, result)
        except:
            responses.noresponse()
    elif "bye" in ui or "exit" in ui or "goodbye" in ui:
        responses.bye()
    else:
        responses.noresponse()