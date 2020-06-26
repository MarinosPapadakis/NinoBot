#Copyright (c) 2020, Marinos Papadakis
#All rights reserved.
#This source code is licensed under the MIT License found in the LICENSE file in the root directory of this source tree.

from responses import *
import responses
import csv
import sqlite3
import webbrowser

# Function to find appropriate response
def findresponse(ui):
    if "hello" in ui or "hi" in ui or "hey" in ui or "yo" in ui:
        greeting()
    elif "years" in ui and "old" and "i" in ui or "years" in ui and "old" and "i'm" in ui or "age" in ui and "my" in ui and "is" in ui:
        for i in range(0, len(ui)):
            try:
                responses.age = int(''.join(itertools.takewhile(lambda s: s.isdigit(), ui[i])))
            except ValueError:
                continue
        typeage()
    elif "capital" in ui and "of" in ui:
        connection = sqlite3.connect("db/country-capitals.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM countrycapitals");
        results = cursor.fetchall()
        connui = ' '.join(ui)
        for r in results:
            if str(r[0]) in str(connui):
                capital(r[1], r[0])
                break
        cursor.close()
        connection.close()
    elif "what's" in ui and "my" in ui and "name" in ui or "what" in ui and "my" in ui and "name" in ui:
        tellusername()
    elif "my" in ui and "name" in ui:
        for i in range(0, len(ui)):
            if "is" == ui[i]:
                break
        try:
            responses.name = ui[i+1]
            typename()
        except:
            noresponse()
    elif "what" in ui and "age" in ui and "my" not in ui or "what's" in ui and "age" in ui and "my" not in ui or "how" in ui and "old" in ui and "are" in ui and "you" in ui:
        howoldareyou()
    elif "how" in ui and "old" in ui and "am" in ui and "i" in ui or "what" in ui and "age" in ui or "whats" in ui and "age" in ui or "what's" in ui and "age" in ui:
        tellage()
    elif "your" in ui and "name" in ui or "tell" in ui and "about" in ui and "you" in ui or "tell" in ui and "about" in ui and "yourself" in ui:
        tellaboutyourself()
    elif "how" in ui and "are" in ui and "you" in ui:
        howareyou()
    elif "not" in ui and "good" in ui:
        whyisthat()
    elif "bad" in ui:
        whyisthat()
    elif "good" in ui or "fine" in ui:
        nicetohear()
    elif "where" in ui and "are" in ui and "from" in ui:
        whereareyoufrom()
    elif ui == "restart":
        restart()
    elif "sorry" in ui:
        sorry()
    elif "you" in ui and "like" in ui and "me" in ui:
        doyoulikeme()
    elif "okay" in ui:
        okay()
    elif "thanks" in ui or "thank" in ui and "you" in ui:
        thanks()
    elif "open" in ui:
        for i in range(0, len(ui)):
            if ui[i] == "open":
                break
        url = f'http://{ui[i+1]}'
        webbrowser.get(using=None).open_new_tab(url)
    elif "find" in ui:
        for i in range(0, len(ui)):
            if ui[i] == "find":
                break
        connui = ' '.join(ui[(i+1):len(ui)])
        url = f'https://www.google.com/search?q={connui}'
        webbrowser.get(using=None).open_new_tab(url)
    elif "bye" in ui or "exit" in ui:
        bye()
    else:
        noresponse()