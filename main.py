import function

while True:
    user_action = input("add, quiz, delete(del) or show: ")
    if user_action == "add":
        while True:
            option = input("noun, verb, sv, other, back: ")
            if option == "b":
                break
            else:
                function.add_new_word(option)

    elif user_action == "quiz":
        while True:
            option = input("Standart dictionary(sd), Strong verbs(sv), back: ")
            if option == "sd":
                lexicon = function.get_lex("standart_words.json")
                tested_words = 0
                passed = 0
                been_nums = []
                while True:
                    [wrd, random_index] = function.get_rand_word(lexicon)
                    if len(been_nums) != len(lexicon):
                        if random_index not in been_nums:
                            been_nums.append(random_index)
                            tested_words += 1
                            if wrd["form"] == "n":
                                user_answer_ingerman = input(f"{wrd['in_georgian']}: ")
                                user_answer_inplural = input("in plural: ")
                                if (user_answer_ingerman != wrd["in_german"] or
                                        user_answer_inplural != wrd["in_german_plural"]):
                                    print(f"Incorrect, your answer: {user_answer_ingerman} - {user_answer_inplural}  / "
                                          f"correct: {random_index + 1}.{wrd["in_german"]} - {wrd['in_german_plural']} "
                                          f" {passed}/{tested_words}")
                                else:
                                    passed += 1
                                    print(f"Correct! {passed}/{tested_words}")
                            elif wrd["form"] == "v":
                                returned = function.quiz_print(wrd, random_index)
                                passed += returned[1]
                                print(f"{returned[0]} - {passed}/{tested_words}")
                            elif wrd["form"] == "o":
                                returned = function.quiz_print(wrd, random_index)
                                passed += returned[1]
                                print(f"{returned[0]} {passed}/{tested_words}")
                        else:
                            print("same")
                            continue
                    else:
                        print(f"Finished, Your score is {passed} from {tested_words}")
                        break
            elif option == "sv":
                lexicon = function.get_lex("sv_dictionary.json")
                tested_words = 0
                passed = 0
                been_nums = []
                while True:
                    [wrd, random_index] = function.get_rand_word(lexicon)
                    if len(been_nums) != len(lexicon):
                        if random_index not in been_nums:
                            been_nums.append(random_index)
                            tested_words += 1
                            user_infintive = input(f"{wrd['in_georgian']} Infinitive: ")
                            user_imperfekt = input("Imperfekt: ")
                            user_partizip2 = input("Partizip II: ")
                            user_hilfsverb = input("Hilfsverb: ")
                            if (wrd["infinitiv"] != user_infintive or wrd["imperfekt"] != user_imperfekt or
                                    wrd["partizip_2"] != user_partizip2 or wrd["hilfsverb"] != user_hilfsverb):
                                print(
                                    f"Incorrect!, your answer: {user_infintive} - {user_imperfekt} - "
                                    f"{user_partizip2} - {user_hilfsverb}  /"
                                    f"correct: {random_index + 1}.{wrd['infinitiv']} - {wrd['imperfekt']} - "
                                    f"{wrd['partizip_2']} - {wrd['hilfsverb']}"
                                    f"{passed}/{tested_words}")
                            else:
                                passed += 1
                                print(f"Correct! {passed}/{tested_words}")
                        else:
                            continue
                    else:
                        print(f"Finished, Your Score is {passed} from {tested_words}")
                        break

            elif option == "b":
                break
    elif user_action == "del":
        while True:
            user_option = input("Standart dictionary(sd), Strong verbs(sv) or back: ")
            if user_option == "sd" or user_option == "sv":
                function.del_word(user_option)
            elif user_option == "b":
                break
    elif user_action == "show":
        user_option = input("Standart dictionary(sd) or Strong verbs(sv): ")
        if user_option == "sd":
            lexicon = function.get_lex("standart_words.json")
            print(len(lexicon))
            for i, w in enumerate(lexicon):
                if w["form"] == "n":
                    print(f"{i + 1}.{w['in_german']} - {w['in_german_plural']} - {w['in_georgian']}")
                elif w["form"] == "v":
                    print(f"{i + 1}.{w['in_german']} - {w['in_georgian']}")
                elif w["form"] == "o":
                    print(f"{i + 1}.{w['in_german']} - {w['in_georgian']}")

        elif user_option == "sv":
            lexicon = function.get_lex("sv_dictionary.json")
            for i, v in enumerate(lexicon):
                print(f"{i + 1}.{v['infinitiv']} - {v['imperfekt']} - {v['partizip_2']} "
                      f"- {v['hilfsverb']} - {v['in_georgian']}")