from telegram import Update
from telegram.ext import (
                          ConversationHandler,  CallbackContext)
from scr.other.keyboard import get_avito_keyboard
from scr.other.metro_dict import metro_dictionary
from scr.model.avito_model import AvitoParser
import scr.other.state as s
from scr.other.logger import debug_requests



@debug_requests
def do_avito(update: Update, context):
    update.message.reply_text(
        text="Напишите название вещи для поиска. Например: BMW",
    )
    return s.AVITO_METRO


@debug_requests
def add_metro(update: Update, context):
    context.user_data['object_for_search'] = update.message.text
    print(context.user_data['object_for_search'])

    update.message.reply_text(
        text="Теперь напишите свое метро",)
    return s.AVITO_TYPE_SORT


@debug_requests
def choose_type_sort(update: Update, context):

    if update.message.text in metro_dictionary:

        context.user_data['metro'] = metro_dictionary[update.message.text]
        print(context.user_data['metro'])
    else:
        update.message.reply_text(text="Такого метро я не знаю. Давй ещё раз.")

        return s.AVITO_TYPE_SORT
    update.message.reply_text(
        text="Теперь выберите порядок сортировки",
        reply_markup=get_avito_keyboard())
    return s.AVITO_FINAL


@debug_requests
def send_result(update: Update, context: CallbackContext):
    chat_id = update.effective_message.chat_id
    sort_type = update.callback_query.data
    avito = AvitoParser(metro=context.user_data['metro'],
                        object_for_search=context.user_data['object_for_search'],
                        sort_type=sort_type)
    i = 0
    context.bot.send_message(chat_id=chat_id, text="searching...")
    answer = avito.get_blocks()
    while i < 7:
        i = i + 1
        text = str(answer[i])
        context.bot.send_message(chat_id=chat_id, text=text)
    context.user_data.clear()
    return ConversationHandler.END


