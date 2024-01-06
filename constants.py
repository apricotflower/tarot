class ErrorMessages:
    QUESTION_VALUE_ERROR = "Please enter a question before picking cards.(请在抽牌前输入问题)"
    CARDS_NEED_VALUE_ERROR = "Invalid input. Please enter a valid number of cards for the spread (请输入正确牌阵所需牌数)。"
    CARD_INDEX_VALUE_ERROR = "Invalid input. Please enter a valid integer (无效输入。请输入正确的数字)。"


class UIConstants:
    ROOT_TITLE = "Tarot Divination"

    QUESTION = "Question(问题):"

    PICK_CARDS = "Pick Cards (抽牌)"

    SHUFFLE = "Shuffle (洗牌)"
    SHUFFLE_RESULT = "Shuffle Result"
    SHUFFLE_FINISH_WIN_WIDTH = 200
    SHUFFLE_FINISH_WIN_HEIGHT = 40
    SHUFFLING_COMPLETE = "Shuffling complete.(洗牌结束)"

    CARDS_NEED = "Please enter the number of cards needed for the spread (请输入牌阵所需牌数):"
    NUMBER_OF_CARDS = "Number of cards in the spread(牌阵牌数): "

    QUIT = "Do you want to quit?(是否退出？)"


class Tarot:
    TAROT_CARDS = {
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
    ORIENTATION_UPRIGHT = "Upright (正)"
    ORIENTATION_REVERSED = "Reversed (逆)"
