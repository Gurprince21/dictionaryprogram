def main():

    import json
    from difflib import get_close_matches
    data = json.load(open("data.json"))

    done = True;
    def translate(word):
        word = word.lower()
        if word in data:
            return data[word]
        elif len(get_close_matches(word, data.keys())) > 0:
            yn = input("Did you mean %s instead? Enter Yes or No " % get_close_matches(word, data.keys())[0])
            if yn == ("yes" or "Yes"):
                return data[get_close_matches(word, data.keys())[0]]
            elif yn == ("no" or "No"):
                return "That is not a word. Please double check it."
            else:
                return "Sorry, we didn't understand your entry."
        else:
            return "The word doesn't exist. Please double check it."


    word = input("Enter word: ")
    print(translate(word))

    again = input("do this program again? ")
    if again == ("yes" or "Yes"):
        main()
    else:
        exit()

main()
