import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:

        while True :
            yn = input(f"Did you mean {get_close_matches(w, data.keys())[0]} instead? Enter Y if yes, or N if no: ").upper()

            if yn == "Y":
                return data[get_close_matches(w, data.keys())[0]]
            elif yn == "N":
                return "The word doesn't exist. Please double check it."
            else:
                print("\nSorry, this is not a valid command.")
    else:
        return "The word doesn't exist. Please double check it."


print("\nThis a simple Dictionary using Python. You can enter a word to find it's definition ! \n")
flag = True

while flag:
    word = input("Enter word: ")
    output = translate(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)

    while True :
        yn = input("\nDo you want to search for more words ? Enter Y if yes, or N if no: ").upper()
        if yn == 'N':
            flag = False
            break
        elif yn != 'Y' :
            print("\nThis is not a valid command !")
        else:
            break

print("Thankyou for using this Dictionary!")
