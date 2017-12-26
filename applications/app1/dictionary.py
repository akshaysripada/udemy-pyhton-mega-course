import json
from difflib import get_close_matches

def get_data(key):
    if key in dictionary:
        return dictionary[key]
    elif key.lower() in dictionary:
        return dictionary[key.lower()]
    elif key.title() in dictionary:
        return dictionary[key.title()]
    elif key.upper() in dictionary:
        return dictionary[key.upper()]
    elif len(get_close_matches(key, dictionary.keys(), n=1, cutoff=0.8)) > 0:
        word = get_close_matches(key, dictionary.keys(), n=1, cutoff=0.8)[0]
        check = input("Did you mean to enter " + word + " Y/y or N/n: ").lower()
        if check == "y":
            return dictionary[word]
        elif check == "n":
            return "Word does not exist. PLease check your entry."
        else:
            return "Invalid entry."
    else:
        return "Word does not exist. PLease check your entry."

filename = "data.json"
dictionary = json.load(open(filename, "r"))

key = input("Enter the word: ")
definitions = get_data(key)

if isinstance(definitions, list):
    for line in definitions:
        print(line)
else:
    print(definitions)
