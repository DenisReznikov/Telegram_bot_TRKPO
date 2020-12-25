from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup

CALLBACK_BUTTON1_YES = "Yes"
CALLBACK_BUTTON2_NO = "No"
CALLBACK_BUTTON3_CAFE = "Кафе"
CALLBACK_BUTTON4_BAR = "Бар"
CALLBACK_BUTTON5_RESTAURANT = "Ресторан"


CALLBACK_BUTTON1_NEWER = "104"
CALLBACK_BUTTON2_CHEAPER = "1"
CALLBACK_BUTTON3_EXPENSIVE = "2"

AVITO_TITLES = {
    CALLBACK_BUTTON1_NEWER: "Новые 🆕",
    CALLBACK_BUTTON2_CHEAPER: "Дешевые",
    CALLBACK_BUTTON3_EXPENSIVE: "Дорогие 🤑",
}

TITLES = {
    CALLBACK_BUTTON1_YES: "Yes 🆗",
    CALLBACK_BUTTON2_NO: "No  🙅‍♂ ",
    CALLBACK_BUTTON3_CAFE: "Cafe ☕ ",
    CALLBACK_BUTTON4_BAR: "Bar 🍺️ ",
    CALLBACK_BUTTON5_RESTAURANT: "Restaurant 🍽️",
}


def get_yes_keyboard():
    keyboard = \
        [
            [
                InlineKeyboardButton(TITLES[CALLBACK_BUTTON1_YES], callback_data=CALLBACK_BUTTON1_YES),
                InlineKeyboardButton(TITLES[CALLBACK_BUTTON2_NO], callback_data=CALLBACK_BUTTON2_NO),
            ],
        ]
    return InlineKeyboardMarkup(keyboard)

def get_avito_keyboard():
    keyboard = \
        [
            [
                InlineKeyboardButton(AVITO_TITLES[CALLBACK_BUTTON2_CHEAPER], callback_data=CALLBACK_BUTTON2_CHEAPER),
                InlineKeyboardButton(AVITO_TITLES[CALLBACK_BUTTON3_EXPENSIVE], callback_data=CALLBACK_BUTTON3_EXPENSIVE)
            ],
            [
                InlineKeyboardButton(AVITO_TITLES[CALLBACK_BUTTON1_NEWER], callback_data=CALLBACK_BUTTON1_NEWER),
            ]
        ]
    return InlineKeyboardMarkup(keyboard)

def get_place_keyboard():
    keyboard = \
        [
            [
                InlineKeyboardButton(TITLES[CALLBACK_BUTTON3_CAFE], callback_data=CALLBACK_BUTTON3_CAFE),
                InlineKeyboardButton(TITLES[CALLBACK_BUTTON4_BAR], callback_data=CALLBACK_BUTTON4_BAR),
            ],
            [
                InlineKeyboardButton(TITLES[CALLBACK_BUTTON5_RESTAURANT], callback_data=CALLBACK_BUTTON5_RESTAURANT),
            ]
        ]
    return InlineKeyboardMarkup(keyboard)