import random
from constants import ErrorMessages,Tarot

# cur_tarot_array = []


# 生成包含不重复数字的长度为78的数组
def shuffle():
    cur_tarot_array = []
    while len(cur_tarot_array) < 78:
        card_num = random.randint(1, 78)
        if not any(card[0] == card_num for card in cur_tarot_array):
            cur_tarot_card = [card_num, random.choice([0, 1])]
            cur_tarot_array.append(cur_tarot_card)
    print(cur_tarot_array)
    return cur_tarot_array


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
        raise ValueError(ErrorMessages.CARDS_NEED_VALUE_ERROR)

    if 1 <= cards_len <= 78:
        return cards_len
    else:
        raise ValueError(ErrorMessages.CARDS_NEED_VALUE_ERROR)


def get_unique_card_indices(index, indices):
    print(index)
    try:
        index = int(index)
    except ValueError:
        raise ValueError(ErrorMessages.CARD_INDEX_VALUE_ERROR)

    if 1 <= index <= 78 and index not in indices:
        return index
    else:
        raise ValueError(ErrorMessages.CARD_INDEX_VALUE_ERROR)


def get_question(question):
    if not question:
        raise ValueError(ErrorMessages.QUESTION_VALUE_ERROR)
    return question


# def pick_cards(question):
#     while True:
#         try:
#             spread_len = get_valid_spread_len(input("\nPlease enter the number of cards needed for the spread ("
#                                                     "请输入牌阵所需牌数): "))
#             break
#         except ValueError as e:
#             pass
#             print(e)
#
#     indices = []
#     while len(indices) < spread_len:
#         i = len(indices) + 1
#         try:
#             index = get_unique_card_indices(input(
#                 f"Choose Card {i},The {ordinal(i)} card. {spread_len} cards totally (第{i}张牌。共{spread_len}张牌):"),
#                                             indices)
#             indices.append(index)
#         except ValueError as e:
#             pass
#             print(e)
#
#     global cur_tarot_array
#     cards_values = [cur_tarot_array[index - 1] for index in indices]
#     print(f"\nQuestion(问题)： {question}")
#     for i, value in enumerate(cards_values, start=1):
#         print(f"The {ordinal(i)} card(第{i}张牌) : {value} {interpret_orientation(value)}")
#
#
# def run():
#     question = input("Question(问题): ")
#     question_finished = False
#     global cur_tarot_array
#     cur_tarot_array = shuffle()
#     while True:
#         try:
#             if question_finished:
#                 question = input("\nQuestion(问题): ")
#                 question_finished = False
#             start_shuffle = input("Shuffle?(Y/N)(是否洗牌？): ").lower()
#             if start_shuffle == "y":
#                 cur_tarot_array = shuffle()
#             elif start_shuffle == "n":
#                 pick_cards(question)
#                 question_finished = True
#             elif start_shuffle == "exit":
#                 break  # exit the loop
#             else:
#                 raise ValueError("Invalid input. Please enter 'Y' or 'N' (or 'exit' to quit).")
#         except ValueError as e:
#             print(e)
#
#
# if __name__ == "__main__":
#     run()
