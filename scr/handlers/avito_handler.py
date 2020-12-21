from telegram import Update
from telegram.ext import (CommandHandler, MessageHandler, Filters,
                          ConversationHandler, CallbackQueryHandler, CallbackContext)
from scr.other.keyboard import get_avito_keyboard
from scr.other.metro_dict import metro_dictionary
from scr.model.avito_model import AvitoParser

METRO, TYPE_SORT = range(2)



def do_avito(update: Update, context):
    print("Sada")
    update.message.reply_text(
        text="Напишите название вещи для поиска. Например: BMW",
    )
    return METRO



def add_metro(update: Update, context):
    context.user_data['object_for_search'] = update.message.text
    update.message.reply_text(
        text="Теперь напишите свое метро",)
    return TYPE_SORT



def choose_type_sort(update: Update, context):
    if update.message.text in metro_dictionary:
        context.user_data['metro'] = metro_dictionary[update.message.text]
    else:
        update.message.reply_text(text="Такого метро я не знаю. Пока 👋")
        context.user_data.clear()
        return ConversationHandler.END
    update.message.reply_text(
        text="Теперь выберите порядок сортировки",
        reply_markup=get_avito_keyboard())


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



def avito_handler():
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('avito', do_avito)],
        states={
            METRO: [MessageHandler(Filters.text, add_metro)],
            TYPE_SORT: [MessageHandler(Filters.text, choose_type_sort)]

        },
        fallbacks=[CallbackQueryHandler(send_result)]
    )
    return conv_handler
