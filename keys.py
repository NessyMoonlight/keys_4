# Case-study #3
# Developers: Borodin Artemiy, Solovyova Maria,
# Selikhova Polina, Lyamin Egor
#

import ru_local as ru


def first():
    '''
    The barrier: Nevill Longbottom.
    '''
    answer = int(input(ru.QUESTION_1))
    match answer:
        case 1 | 3:
            question_1 = 0
        case 2:
            question_1 = answer
    return True if question_1 == 2 else False


def second():
    '''
    The barrier: Three-headed dog Fluff.
    '''
    answer = int(input(ru.QUESTION_2))
    match answer:
        case 2 | 4:
            question_2 = 0
        case 1 | 3:
            question_2 = answer
    return True if question_2 == 1 or 3 else False


def third():
    '''
    The barrier: The trapdoor
    with the devil's snares.
    '''
    answer = int(input(ru.QUESTION_3))
    match answer:
        case 2 | 3:
            question_3 = 0
        case 1:
            question_3 = answer
    return True if question_3 == 1 else False


def fourth():
    '''
    The barrier: Key extraction.
    '''
    answer = int(input(ru.QUESTION_4))
    match answer:
        case 1 | 2:
            question_4 = 0
        case 3:
            question_4 = answer
    if question_4 != 3:
        return False
    else:
        answer = int(input(ru.QUESTION_5))
        match answer:
            case 1 | 2:
                question_5 = 0
            case 3:
                question_5 = answer
        return True if question_5 == 3 else False

def fifth():
    '''
    The barrier: Dangerous chess.
    '''
    answer = int(input(ru.QUESTION_6))
    match answer:
        case 1 | 3:
            question_6 = 0
        case 2 | 4:
            question_6 = answer
    if question_6 != 2 or question_6 != 4:
        return False
    else:
        answer = int(input(ru.QUESTION_7))
        match answer:
            case 1 | 2:
                question_7 = 0
            case 3:
                question_7 = answer
        if question_7 != 3:
            return False
        else:
            answer = int(input(ru.QUESTION_8))
            match answer:
                case 1:
                    question_8 = 0
                case 2:
                    question_8 = answer
            return True if question_8 == 2 else False


def sixth():
    '''
    The barrier: Poison and water.
    '''
    answer = int(input(ru.QUESTION_9))
    match answer:
        case 2 | 3 | 4 | 5:
            question_9 = 0
        case 1 | 6:
            question_9 = answer
    if question_9 != 1 or question_7 != 6:
        return False
    else:
        answer = int(input(ru.QUESTION_10))
        match answer:
            case 1 | 3:
                question_10 = 0
            case 2:
                question_10 = answer
        return True if question_10 == 2 else False


def seventh():
    '''
    The barrier: The traitor Quirell.
    '''
    answer = int(input(ru.QUESTION_11))
    match answer:
        case 1:
            question_11 = 0
        case 2:
            question_11 = answer
    return True if question_11 == 2 else False


def eighth():
    '''
    The barrier: The mirrow Einalege.
    '''
    answer = int(input(ru.QUESTION_12))
    match answer:
        case 1 | 2:
            question_12 = 0
        case 3:
            question_12 = answer
    return True if question_12 == 3 else False


def ninth():
    '''
    The barrier: An unexpected chance.
    '''
    answer = int(input(ru.QUESTION_13))
    match answer:
        case 1:
            question_13 = 0
        case 2:
            question_13 = answer
    return True if question_13 == 2 else False



def main():
    '''
    Main function.
    '''
if (first() and second() and third() and fourth() and fifth() \
    and sixth() and seventh() and eighth() and ninth()) == True:
    print(ru.END)
else:
    print(ru.NEGATIVE)


if __name__ == '__main__':
    main()
