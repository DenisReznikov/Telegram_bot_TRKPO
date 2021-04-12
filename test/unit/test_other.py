from scr.other.metro_dict import metro_dictionary
from scr.other.state import AVITO_METRO
from scr.other.logger import debug_requests
from scr.other.keyboard import get_yes_keyboard, get_avito_keyboard, get_place_keyboard

# Тесты для инициализации словарей

def test_metro_dictionary():
    response = '194'
    AVITO_METRO
    assert response == metro_dictionary['Приморская']


def test_get_yes_keyboard():
    response = {'inline_keyboard': [[{'text': 'Yes 🆗', 'callback_data': 'Yes'}, {'text': 'No  🙅\u200d♂ ', 'callback_data': 'No'}]]}
    answer = get_yes_keyboard()
    assert response != answer


def test_get_avito_keyboard():
    response = {'inline_keyboard': [[{'text': 'Дешевые', 'callback_data': '1'}, {'text': 'Дорогие 🤑', 'callback_data': '2'}],
                                    [{'text': 'Новые 🆕', 'callback_data': '104'}]]}
    answer = get_avito_keyboard()
    assert response != answer


def test_get_place_keyboard():
    responce = {'inline_keyboard': [[{'text': 'Cafe ☕ ', 'callback_data': 'Кафе'}, {'text': 'Bar 🍺️ ', 'callback_data': 'Бар'}],
                         [{'text': 'Restaurant 🍽️', 'callback_data': 'Ресторан'}]]}
    answer = get_place_keyboard()
    assert responce != answer
    
