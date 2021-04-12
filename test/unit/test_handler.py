import math
from datetime import datetime
from telegram import Update, Chat, User, Bot, Location
from telegram import Message, MessageEntity, CallbackQuery

from handlers.handler_weather import do_start_weather, do_location, do_city, do_done
from handlers.handler_eat import do_eat, button, do_done, do_more_eat
from handlers.avito_handler import do_avito, add_metro, choose_type_sort, send_result

from handlers import handler_eat
from handlers import handler_weather
from other.keyboard import get_place_keyboard


def test_do_start_weather():
    message = Message(
        message_id=1,
        chat=Chat(405052764, 'private'),
        date=None,
        from_user=User(0, 'user', False),
        text='Москва',
        location=Location(30.35, 59.98),
        entities=[
            MessageEntity(type=MessageEntity.BOT_COMMAND, offset=0, length=len('/weather'))
        ],
        bot=Bot(token='1486083484:AAEBHCVAtKRQRD0neNbem7NgrUAnbIo2enU'),
    )

    class Context:
        user_data = {}

    update = Update(update_id=0, message=message)
    answer = do_start_weather(update, 0)
    assert answer == 5


def test_do_location():
    message = Message(
        message_id=1,
        chat=Chat(405052764, 'private'),
        date=None,
        from_user=User(0, 'user', False),
        text='Москва',
        location=Location(30.35, 59.98),
        entities=[
            MessageEntity(type=MessageEntity.BOT_COMMAND, offset=0, length=len('/weather'))
        ],
        bot=Bot(token='1486083484:AAEBHCVAtKRQRD0neNbem7NgrUAnbIo2enU'),
    )

    class Context:
        user_data = {}

    update = Update(update_id=0, message=message)
    answer = do_location(update, Context)
    assert answer == 6


def test_do_city():
    message = Message(
        message_id=1,
        chat=Chat(405052764, 'private'),
        date=None,
        from_user=User(0, 'user', False),
        text='Москва',
        entities=[
            MessageEntity(type=MessageEntity.BOT_COMMAND, offset=0, length=len('/weather'))
        ],
        bot=Bot(token='1486083484:AAEBHCVAtKRQRD0neNbem7NgrUAnbIo2enU'),
    )

    class Context:
        user_data = {}

    update = Update(update_id=0, message=message)
    answer = do_city(update, Context)
    assert answer == 6


def test_do_city_v2():
    message = Message(
        message_id=1,
        chat=Chat(405052764, 'private'),
        date=None,
        from_user=User(0, 'user', False),
        text='text',
        entities=[
            MessageEntity(type=MessageEntity.BOT_COMMAND, offset=0, length=len('/weather'))
        ],
        bot=Bot(token='1486083484:AAEBHCVAtKRQRD0neNbem7NgrUAnbIo2enU'),
    )

    class Context:
        user_data = {}

    update = Update(update_id=0, message=message)
    answer = do_city(update, Context)
    assert answer == 5


def test_do_done_weather():
    message = Message(
        message_id=1,
        chat=Chat(405052764, 'private'),
        date=int(math.floor(datetime.timestamp(datetime.today()))),
        from_user=User(0, 'user', False),
        text='Yes',
        location=Location(30.35, 59.98),
        entities=[
            MessageEntity(type=MessageEntity.BOT_COMMAND, offset=0, length=len('/weather'))
        ],
        bot=Bot(token='1486083484:AAEBHCVAtKRQRD0neNbem7NgrUAnbIo2enU'),
    )

    callbackquery = CallbackQuery(
        id=1,
        from_user=User(0, 'user', False),
        chat_instance=1337,
        data='Yes'
    )

    class Context:
        user_data = dict(longitude='30.35', latitude='59.98', city='')
        bot = Bot(token='1486083484:AAEBHCVAtKRQRD0neNbem7NgrUAnbIo2enU')

    update = Update(
        update_id=0,
        message=message,
        callback_query=callbackquery
    )
    answer = handler_weather.do_done(update, Context)
    assert answer == -1


# ----------------------------------------------------------------

def test_do_eat():
    message = Message(
        message_id=1,
        chat=Chat(405052764, 'private'),
        date=None,
        from_user=User(0, 'user', False),
        text='Москва',
        location=Location(30.35, 59.98),
        entities=[
            MessageEntity(type=MessageEntity.BOT_COMMAND, offset=0, length=len('/eat'))
        ],
        bot=Bot(token='1486083484:AAEBHCVAtKRQRD0neNbem7NgrUAnbIo2enU'),
    )

    class Context:
        user_data = {}

    update = Update(update_id=0, message=message)
    answer = do_eat(update, 0)
    assert answer == 7


def test_do_done_eat_pos():
    message = Message(
        message_id=1,
        chat=Chat(405052764, 'private'),
        date=None,
        from_user=User(0, 'user', False),
        text='Москва',
        location=Location(30.35, 59.98),
        entities=[
            MessageEntity(type=MessageEntity.BOT_COMMAND, offset=0, length=len('/eat'))
        ],
        bot=Bot(token='1486083484:AAEBHCVAtKRQRD0neNbem7NgrUAnbIo2enU'),
    )

    class Context:
        user_data = dict(choice='Кафе',
                         longitude='30.35',
                         latitude='59.98'
                         )

    update = Update(update_id=0, message=message)
    answer = handler_eat.do_done(update, Context)
    assert answer == 9


def test_do_done_eat_neg():
    message = Message(
        message_id=1,
        chat=Chat(405052764, 'private'),
        date=None,
        from_user=User(0, 'user', False),
        text='Москва',
        location=Location(30.35, 59.98),
        entities=[
            MessageEntity(type=MessageEntity.BOT_COMMAND, offset=0, length=len('/eat'))
        ],
        bot=Bot(token='1486083484:AAEBHCVAtKRQRD0neNbem7NgrUAnbIo2enU'),
    )

    class Context:
        user_data = dict(choice='Бар',
                         longitude='30.35',
                         latitude='59.98'
                         )

    update = Update(update_id=0, message=message)
    answer = handler_eat.do_done(update, Context)
    assert answer == -1


def test_button():
    message = Message(
        message_id=5211,
        chat=Chat(405052764, 'private'),
        date=int(math.floor(datetime.timestamp(datetime.today()))),
        from_user=User(id=1486083484, first_name='Finder Bot', is_bot=True, username='trpko_70115_bot'),
        text='Выберети категорию.',
        location=Location(30.35, 59.98),
        entities=[
            MessageEntity(type=MessageEntity.BOT_COMMAND, offset=0, length=len('/eat'))
        ],
        bot=Bot(token='1486083484:AAEBHCVAtKRQRD0neNbem7NgrUAnbIo2enU'),
    )
    callbackquery = CallbackQuery(
        id='1739688375581554767',
        from_user=User(405052764, 'Vlad', False, 'ru'),
        chat_instance='3132093361670597037',
        message=message,
        bot=Bot(token='1486083484:AAEBHCVAtKRQRD0neNbem7NgrUAnbIo2enU')
    )

    class Context:
        user_data = {}
        bot = Bot(token='1486083484:AAEBHCVAtKRQRD0neNbem7NgrUAnbIo2enU')

    update = Update(
        update_id=0,
        message=message,
        callback_query=callbackquery
    )
    update.message.edit_text(text="Выберети категорию.",
                             reply_markup=get_place_keyboard())
    answer = button(update, Context)
    assert answer == 8


def test_do_more_eat():
    message = Message(
        message_id=1,
        chat=Chat(405052764, 'private'),
        date=None,
        from_user=User(0, 'user', False),
        text='Москва',
        location=Location(30.35, 59.98),
        entities=[
            MessageEntity(type=MessageEntity.BOT_COMMAND, offset=0, length=len('/eat'))
        ],
        bot=Bot(token='1486083484:AAEBHCVAtKRQRD0neNbem7NgrUAnbIo2enU'),
    )

    class Context:
        user_data = dict(choice='Кафе',
                         longitude='30.35',
                         latitude='59.98')

    update = Update(update_id=0, message=message)
    answer = do_more_eat(update, Context)
    assert answer == -1


def test_do_more_eat_v2():
    message = Message(
        message_id=1,
        chat=Chat(405052764, 'private'),
        date=None,
        from_user=User(0, 'user', False),
        text='Москва',
        location=Location(30.35, 59.98),
        entities=[
            MessageEntity(type=MessageEntity.BOT_COMMAND, offset=0, length=len('/eat'))
        ],
        bot=Bot(token='1486083484:AAEBHCVAtKRQRD0neNbem7NgrUAnbIo2enU'),
    )

    class Context:
        user_data = dict(choice='Бар',
                         longitude='30.35',
                         latitude='59.98')

    update = Update(update_id=0, message=message)
    answer = do_more_eat(update, Context)
    assert answer == -1


# -----------------------------------------------------------------

def test_do_avito():
    message = Message(
        message_id=1,
        chat=Chat(405052764, 'private'),
        date=None,
        from_user=User(0, 'user', False),
        text='Москва',
        location=Location(30.35, 59.98),
        entities=[
            MessageEntity(type=MessageEntity.BOT_COMMAND, offset=0, length=len('/avito'))
        ],
        bot=Bot(token='1486083484:AAEBHCVAtKRQRD0neNbem7NgrUAnbIo2enU'),
    )

    class Context:
        user_data = {}

    update = Update(update_id=0, message=message)
    answer = do_avito(update, 0)
    assert answer == 0


def test_add_metro():
    message = Message(
        message_id=1,
        chat=Chat(405052764, 'private'),
        date=None,
        from_user=User(0, 'user', False),
        text='Москва',
        location=Location(30.35, 59.98),
        entities=[
            MessageEntity(type=MessageEntity.BOT_COMMAND, offset=0, length=len('/avito'))
        ],
        bot=Bot(token='1486083484:AAEBHCVAtKRQRD0neNbem7NgrUAnbIo2enU'),
    )

    class Context:
        user_data = dict(object_for_search='159')

    update = Update(update_id=0, message=message)
    answer = add_metro(update, Context)
    assert answer == 1


def test_choose_type_sort():
    message = Message(
        message_id=1,
        chat=Chat(405052764, 'private'),
        date=None,
        from_user=User(0, 'user', False),
        text='Девяткино',
        location=Location(30.35, 59.98),
        entities=[
            MessageEntity(type=MessageEntity.BOT_COMMAND, offset=0, length=len('/avito'))
        ],
        bot=Bot(token='1486083484:AAEBHCVAtKRQRD0neNbem7NgrUAnbIo2enU'),
    )

    class Context:
        user_data = dict(metro='159')

    update = Update(update_id=0, message=message)
    answer = choose_type_sort(update, Context)
    assert answer == 3


def test_choose_type_sort_v2():
    message = Message(
        message_id=1,
        chat=Chat(405052764, 'private'),
        date=None,
        from_user=User(0, 'user', False),
        text='Столичное',
        location=Location(30.35, 59.98),
        entities=[
            MessageEntity(type=MessageEntity.BOT_COMMAND, offset=0, length=len('/avito'))
        ],
        bot=Bot(token='1486083484:AAEBHCVAtKRQRD0neNbem7NgrUAnbIo2enU'),
    )

    class Context:
        user_data = dict(metro='159')

    update = Update(update_id=0, message=message)
    answer = choose_type_sort(update, Context)
    assert answer == 1


def test_send_result():
    message = Message(
        message_id=1,
        chat=Chat(405052764, 'private'),
        date=int(math.floor(datetime.timestamp(datetime.today()))),
        from_user=User(0, 'user', False),
        text='Yes',
        location=Location(30.35, 59.98),
        entities=[
            MessageEntity(type=MessageEntity.BOT_COMMAND, offset=0, length=len('/weather'))
        ],
        bot=Bot(token='1486083484:AAEBHCVAtKRQRD0neNbem7NgrUAnbIo2enU'),
    )

    callbackquery = CallbackQuery(
        id=1,
        from_user=User(0, 'user', False),
        chat_instance=1337,
        data='Yes'
    )

    class Context:
        user_data = dict(metro=159, object_for_search='naruto', sort_type=1)
        bot = Bot(token='1486083484:AAEBHCVAtKRQRD0neNbem7NgrUAnbIo2enU')

    update = Update(
        update_id=0,
        message=message,
        callback_query=callbackquery
    )
    answer = send_result(update, Context)
    assert answer == -1
