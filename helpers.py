import itertools

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

# Function to find word in list
def findword(word, list):
    for i in range(0, len(list)):
        if list[i] == word:
            return i
    return None
