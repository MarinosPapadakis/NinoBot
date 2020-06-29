#Copyright (c) 2020, Marinos Papadakis
#All rights reserved.
#This source code is licensed under the MIT License found in the LICENSE file in the root directory of this source tree.

from responses import *
import responses
import csv
import sqlite3
import webbrowser
import math
from simpleeval import simple_eval

# Function to return number from list
def findnumber(list):
    number = None
    for i in range(0, len(list)):
        try:
            number = int(''.join(itertools.takewhile(lambda s: s.isdigit(), list[i])))
            break
        except ValueError:
            continue
    return number

# Function to see if string is number
def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

# Function to find appropriate response
def findresponse(ui):
    if "hello" in ui or "hi" in ui or "hey" in ui or "yo" in ui:
        greeting()
    elif "years" in ui and "old" and "i" in ui or "years" in ui and "old" and "i'm" in ui or "age" in ui and "my" in ui and "is" in ui:
        responses.age = findnumber(ui)
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
    elif "my" in ui and "name" in ui or "my" in ui and "name's" in ui:
        for i in range(0, len(ui)):
            if "is" == ui[i] or "name's" == ui[i]:
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
            domath(str_r, result)
        except:
            noresponse()
    elif "square" in ui and "root" in ui or "√" in ui:
        n = findnumber(ui)
        if n:
            sqrt = math.sqrt(n)
            squareroot(n, sqrt)
        else:
            noresponse()
    elif "raised" in ui and "to" in ui and "power" in ui:
        for n in range(0, len(ui)):
            if ui[n] == "raised":
                break
        for i in range(0, len(ui)):
            if ui[i] == "of":
                break
        try:
            if (n-1) >= 0:
                num1 = ui[n-1]
            else:
                num1 = None
            num2 = ui[i+1]
            num1 = int(num1)
            num2 = int(num2)
            result = pow(num1, num2)
            powerof(num1, num2, result)
        except:
            noresponse()
    elif "bye" in ui or "exit" in ui:
        bye()
    else:
        noresponse()