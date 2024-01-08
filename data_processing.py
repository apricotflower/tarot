import random
from constants import ErrorMessages,Tarot

cur_tarot_array = []


# 生成包含不重复数字的长度为78的数组
def shuffle():
    tarot_array = []
    while len(tarot_array) < Tarot.TAROT_LEN:
        card_num = random.randint(1, Tarot.TAROT_LEN)
        if not any(card[0] == card_num for card in tarot_array):
            cur_tarot_card = [card_num, random.choice([0, 1])]
            tarot_array.append(cur_tarot_card)
    print(tarot_array)
    global cur_tarot_array
    cur_tarot_array = tarot_array
    return tarot_array


def interpret_orientation(value):
    card_number = value[0]
    orientation = Tarot.ORIENTATION_REVERSED if value[1] == 0 else Tarot.ORIENTATION_UPRIGHT
    return f"{Tarot.TAROT_CARDS.get(card_number, 'card')} {orientation}"


def ordinal(number):
    if 10 <= number % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(number % 10, 'th')
    return f"{number}{suffix}"


def get_valid_spread_len(cards_len):
    try:
        cards_len = int(cards_len)
    except ValueError:
        raise ValueError(ErrorMessages.CARDS_NEED_VALUE_ERROR.format(cards_len))

    if 1 <= cards_len <= Tarot.TAROT_LEN:
        return cards_len
    else:
        raise ValueError(ErrorMessages.CARDS_NEED_VALUE_ERROR.format(cards_len))


def get_unique_card_value(index, cards_value):
    global cur_tarot_array
    try:
        index = int(index)
    except ValueError:
        raise ValueError(ErrorMessages.CARD_INDEX_VALUE_ERROR.format(index))

    if 1 <= index <= Tarot.TAROT_LEN and index not in cards_value:
        card_value = [index, interpret_orientation(cur_tarot_array[index - 1])]
        return card_value
    else:
        raise ValueError(ErrorMessages.CARD_INDEX_VALUE_ERROR.format(index))


def get_question(question):
    if not question:
        raise ValueError(ErrorMessages.QUESTION_VALUE_ERROR)
    return question
