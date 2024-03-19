# Case-study #3
# Developers: Borodin Artemiy, Solovyova Maria,
# Selikhova Polina, Lyamin Egor
#

import ru_local as ru

question_1 = input(ru.QUESTION_1)
if question_1 == '2':
    question_2 = input(ru.QUESTION_2)
    if question_2 == '1' or question_2 == '3':
        question_3 = input(ru.QUESTION_3)
        if question_3 == '1':
            question_4 = input(ru.QUESTION_4)
            if question_4 == '3':
                question_5 = input(ru.QUESTION_5)
                if question_5 == '3':
                    question_6 = input(ru.QUESTION_6)
                    if question_6 == '2':
                        question_7 = input(ru.QUESTION_7)
                        if question_7 == '3':
                            question_8 = input(ru.QUESTION_8)
                            if question_8 == '2':
                                question_9 = input(ru.QUESTION_9)
                                if question_9 == '1 6' or question_9 == '6 1':
                                    question_10 = input(ru.QUESTION_10)
                                    if question_10 == '2':
                                        question_11 = input(ru.QUESTION_11)
                                        if question_11 == '2':
                                            question_12 = input(ru.QUESTION_12)
                                            if question_12 == '3':
                                                question_13 = input(ru.QUESTION_13)
                                                if question_13 == '2':
                                                    print(ru.END)
else:
    print(ru.NEGATIVE)


if __name__ == '__main__':
    main()
