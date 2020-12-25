from telegram import Update
from telegram.ext import (CommandHandler, MessageHandler, Filters,
                          ConversationHandler, CallbackQueryHandler, CallbackContext)
from scr.model.api_for_eat import search
from scr.other.keyboard import get_place_keyboard
from scr.other.logger import debug_requests
import scr.other.state as s
CHOOSING = range(1)

@debug_requests
def do_eat(update: Update, context):
    update.message.reply_text(
        text="Выберети категорию.",
        reply_markup=get_place_keyboard()
    )
    return s.CHOOSING_EAT


@debug_requests
def button(update: Update, context: CallbackContext):
    context.user_data['choice'] = update.callback_query.data
    update.callback_query.edit_message_text(
        text="Отправьте свою геопозицию",
    )
    return s.RESULT_EAT


@debug_requests
def do_done(update: Update, context):
    i = 0
    count = 3
    type_of_place = context.user_data['choice']

    longitude, latitude = update.message.location.longitude, update.message.location.latitude
    context.user_data['longitude'],context.user_data['latitude'] = longitude, latitude
    result = search(type_of_place, longitude, latitude, count= count)
    print((result))
    print(("_______"))
    if isinstance(result, dict):
        while i < count:
            answer = result[str(i) + 'answer']
            longitude = result[str(i) + 'longitude']
            latitude = result[str(i) + 'latitude']
            update.message.reply_text(text=answer)
            update.message.reply_location(longitude=longitude, latitude=latitude)
            i += 1
        update.message.reply_text(text="Увеличить радиус поиска -> /more \n\n"
                                       "закончить беседу /end")
        return s.MORE_EAT

    if result == 1:
        update.message.reply_text(text="Увеличить радиус поиска -> /more")
        return s.MORE_EAT
    if result == 0:
        update.message.reply_text(text="Api yandex сломалось, попробуйте ещё раз позже. ")
        return ConversationHandler.END




@debug_requests
def do_more_eat(update: Update, context):
    i = 3
    count = 5
    type_of_place = context.user_data['choice']
    longitude, latitude = context.user_data['longitude'],context.user_data['latitude']
    result = search(type_of_place, longitude, latitude,range=0.5, count=count)
    print((result))
    print(("_______"))
    if isinstance(result, dict):
        while i < count:
            answer = result[str(i) + 'answer']
            longitude = result[str(i) + 'longitude']
            latitude = result[str(i) + 'latitude']
            update.message.reply_text(text=answer)
            update.message.reply_location(longitude=longitude, latitude=latitude)
            i += 1
        update.message.reply_text(text="Пока")
        return ConversationHandler.END

    else:
        update.message.reply_text(text="Api yandex сломалось, попробуйте ещё раз позже. ")
        return ConversationHandler.END


