import random


# cur_tarot_array = []


# 生成包含不重复数字的长度为78的数组
def shuffle(cur_tarot_array):
    # global cur_tarot_array
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

    tarot_cards = {
        1: "The Magician (魔术师)",
        2: "The High Priestess (女祭司)",
        3: "The Empress (皇后)",
        4: "The Emperor (皇帝)",
        5: "The Hierophant (教皇)",
        6: "The Lovers (恋人)",
        7: "The Chariot (战车)",
        8: "Strength (力量)",
        9: "The Hermit (隐士)",
        10: "Wheel of Fortune (命运之轮)",
        11: "Justice (正义)",
        12: "The Hanged Man (吊人)",
        13: "Death (死神)",
        14: "Temperance (节制)",
        15: "The Devil (恶魔)",
        16: "The Tower (塔)",
        17: "The Star (星星)",
        18: "The Moon (月亮)",
        19: "The Sun (太阳)",
        20: "Judgment (审判)",
        21: "The World (世界)",
        22: "The Fool (愚人)",
        23: "Ace of Wands (权杖一)",
        24: "Two of Wands (权杖二)",
        25: "Three of Wands (权杖三)",
        26: "Four of Wands (权杖四)",
        27: "Five of Wands (权杖五)",
        28: "Six of Wands (权杖六)",
        29: "Seven of Wands (权杖七)",
        30: "Eight of Wands (权杖八)",
        31: "Nine of Wands (权杖九)",
        32: "Ten of Wands (权杖十)",
        33: "Page of Wands (权杖侍者)",
        34: "Knight of Wands (权杖骑士)",
        35: "Queen of Wands (权杖王后)",
        36: "King of Wands (权杖国王)",
        37: "Ace of Cups (圣杯一)",
        38: "Two of Cups (圣杯二)",
        39: "Three of Cups (圣杯三)",
        40: "Four of Cups (圣杯四)",
        41: "Five of Cups (圣杯五)",
        42: "Six of Cups (圣杯六)",
        43: "Seven of Cups (圣杯七)",
        44: "Eight of Cups (圣杯八)",
        45: "Nine of Cups (圣杯九)",
        46: "Ten of Cups (圣杯十)",
        47: "Page of Cups (圣杯侍者)",
        48: "Knight of Cups (圣杯骑士)",
        49: "Queen of Cups (圣杯王后)",
        50: "King of Cups (圣杯国王)",
        51: "Ace of Swords (宝剑一)",
        52: "Two of Swords (宝剑二)",
        53: "Three of Swords (宝剑三)",
        54: "Four of Swords (宝剑四)",
        55: "Five of Swords (宝剑五)",
        56: "Six of Swords (宝剑六)",
        57: "Seven of Swords (宝剑七)",
        58: "Eight of Swords (宝剑八)",
        59: "Nine of Swords (宝剑九)",
        60: "Ten of Swords (宝剑十)",
        61: "Page of Swords (宝剑侍者)",
        62: "Knight of Swords (宝剑骑士)",
        63: "Queen of Swords (宝剑王后)",
        64: "King of Swords (宝剑国王)",
        65: "Ace of Pentacles (星币一)",
        66: "Two of Pentacles (星币二)",
        67: "Three of Pentacles (星币三)",
        68: "Four of Pentacles (星币四)",
        69: "Five of Pentacles (星币五)",
        70: "Six of Pentacles (星币六)",
        71: "Seven of Pentacles (星币七)",
        72: "Eight of Pentacles (星币八)",
        73: "Nine of Pentacles (星币九)",
        74: "Ten of Pentacles (星币十)",
        75: "Page of Pentacles (星币侍者)",
        76: "Knight of Pentacles (星币骑士)",
        77: "Queen of Pentacles (星币王后)",
        78: "King of Pentacles (星币国王)"
    }
    orientation = "Reversed (逆)" if value[1] == 0 else "Upright (正)"
    return f"{tarot_cards.get(card_number, 'card')} {orientation}"


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
        raise ValueError("Invalid input. Please enter a valid number of cards for the spread (请输入正确牌阵所需牌数)。")

    if 1 <= cards_len <= 78:
        return cards_len
    else:
        raise ValueError("Invalid input. Please enter a valid number of cards for the spread (请输入正确牌阵所需牌数)。")


def get_unique_card_indices(spread_len):
    indices = []
    while len(indices) < spread_len:
        i = len(indices) + 1
        try:
            index = int(input(f"The {ordinal(i)} card(第{i}张牌): "))
            if 1 <= index <= 78 and index not in indices:
                indices.append(index)
            else:
                raise ValueError("Invalid input. Please enter a valid integer (无效输入。请输入正确的数字)。")
        except ValueError as e:
            pass
            print(e)
    return indices


def pick_cards(question, cur_tarot_array):
    while True:
        try:
            spread_len = get_valid_spread_len(input("\nPlease enter the number of cards needed for the spread ("
                                                    "请输入牌阵所需牌数): "))
            break
        except ValueError as e:
            pass
            print(e)

    indices = get_unique_card_indices(spread_len)

    cards_values = [cur_tarot_array[index - 1] for index in indices]
    print(f"\nQuestion(问题)： {question}")
    for i, value in enumerate(cards_values, start=1):
        print(f"The {ordinal(i)} card(第{i}张牌) : {value} {interpret_orientation(value)}")


def run():
    question = input("Question(问题): ")
    question_finished = False
    # global cur_tarot_array
    cur_tarot_array = []
    cur_tarot_array = shuffle(cur_tarot_array)
    while True:
        try:
            if question_finished:
                question = input("\nQuestion(问题): ")
                question_finished = False
            start_shuffle = input("Shuffle?(Y/N)(是否洗牌？): ").lower()
            if start_shuffle == "y":
                shuffle(cur_tarot_array)
            elif start_shuffle == "n":
                pick_cards(question, cur_tarot_array)
                question_finished = True
            elif start_shuffle == "exit":
                break  # exit the loop
            else:
                raise ValueError("Invalid input. Please enter 'Y' or 'N' (or 'exit' to quit).")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    run()
