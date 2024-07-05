import json
import random


def add_new_word(option):
    word = {}
    if option == "n":
        in_german = input("Enter noun in German: ")
        in_german_plural = input("Enter noun in plural: ")
        in_georgian = input("Enter noun in Georgian: ")
        word = {
            "form": option,
            "in_german": in_german,
            "in_german_plural": in_german_plural,
            "in_georgian": in_georgian
        }

    elif option == "v":
        in_german = input("Enter verb in German: ")
        in_georgian = input("Enter verb in Georgian: ")
        word = {
            "form": option,
            "in_german": in_german,
            "in_georgian": in_georgian
        }

    elif option == "sv":
        infinitiv = input("Infinitiv: ")
        imperfekt = input("Imperfekt: ")
        partizip_2 = input("Partizip II: ")
        hilfsverb = input("Hilfsverb: ")
        in_georgian = input("In Georgian: ")

        word = {
            "form": option,
            "infinitiv": infinitiv,
            "imperfekt": imperfekt,
            "partizip_2": partizip_2,
            "hilfsverb": hilfsverb,
            "in_georgian": in_georgian
        }

    elif option == "o":
        sentence = input("Enter sentence in German: ")
        in_georgian = input("Enter in Georgian: ")
        word = {
            "form": option,
            "in_german": sentence,
            "in_georgian": in_georgian
        }

    try:
        lexicon = get_lex("standart_words.json" if option in ["n", "v", "o"] else "sv_dictionary.json")
        lexicon.append(word)
        with open("standart_words.json" if option in ["n", "v", "o"] else "sv_dictionary.json", "w") as file:
            json.dump(lexicon, file)
        ind_numb = len(lexicon)

        if word["form"] == "n":
            print(f"Added: {ind_numb}.{word['in_german']} - {word['in_german_plural']} - {word['in_georgian']}")
        elif word["form"] == "v":
            print(f"Added: {ind_numb}.{word['in_german']} - {word['in_georgian']}")
        elif word["form"] == "o":
            print(f"Added: {ind_numb}.{word['in_german']} - {word['in_georgian']}")
        elif word["form"] == "sv":
            print(
                f"Added: {ind_numb}.{word['infinitiv']} - {word['imperfekt']} - {word['partizip_2']} - {word['hilfsverb']} - {word['in_georgian']}")
    except KeyError:
        print("Unknown command")


def del_word(opt):
    try:
        ind1 = int(input("Enter number to delete: ")) - 1
        if ind1 < 0:
            print("Enter more than 0")
            return
        if opt == "sd":
            lexicon = get_lex("standart_words.json")
            deleted = lexicon.pop(ind1)
            print(len(lexicon))
            with open("standart_words.json", "w") as file:
                json.dump(lexicon, file)
                print(f"Deleted - {deleted['in_german']}")
        elif opt == "sv":
            lexicon = get_lex("sv_dictionary.json")
            deleted = lexicon.pop(ind1)
            with open("sv_dictionary.json", "w") as file:
                json.dump(lexicon, file)
            print(f"Deleted {deleted['infinitiv']}")
    except ValueError:
        print("Enter only numbers")
    except IndexError:
        print("Number ot of range")


def quiz_print(w, random_index):
    user_answeringerman = input(f"{w['in_georgian']}: ")
    if w["in_german"] != user_answeringerman:
        return [f"Incorrect, your answer: {user_answeringerman} / " 
                f"correct: {random_index + 1}.{w['in_german']}", 0]

    else:
        return ["Correct!", 1]


def get_rand_word(lxcn):
    rand_index = random.randint(0, len(lxcn) - 1)
    rand_wrd = lxcn[rand_index]
    return [rand_wrd, rand_index]


def get_lex(filepath):
    with open(filepath, "r") as file:
        content = file.read()
    data = json.loads(content)
    return data
