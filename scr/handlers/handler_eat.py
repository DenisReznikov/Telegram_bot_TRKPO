from telegram import Update
from telegram.ext import (CommandHandler, MessageHandler, Filters,
                          ConversationHandler, CallbackQueryHandler, CallbackContext)
from scr.model.api_for_eat import search
from scr.other.keyboard import get_place_keyboard
from scr.other.logger import debug_requests

CHOOSING = range(1)

@debug_requests
def do_eat(update: Update, context):
    update.message.reply_text(
        text="Select a category to search.",
        reply_markup=get_place_keyboard()
    )
    return CHOOSING


@debug_requests
def button(update: Update, context: CallbackContext):
    context.user_data['choice'] = update.callback_query.data
    update.callback_query.edit_message_text(
        text="Send U location",
    )


@debug_requests
def do_done(update: Update, context):
    i = 0
    type_of_place = context.user_data['choice']
    longitude, latitude = update.message.location.longitude, update.message.location.latitude
    result = search(type_of_place, longitude, latitude)
    while i < 3:
        answer = result[str(i) + 'answer']
        longitude = result[str(i) + 'longitude']
        latitude = result[str(i) + 'latitude']
        update.message.reply_text(text=answer)
        update.message.reply_location(longitude=longitude, latitude=latitude)
        i += 1
    context.user_data.clear()
    return ConversationHandler.END


def eat_handler():
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('eat', do_eat)],
        states={CHOOSING: [CallbackQueryHandler(button)]},
        fallbacks=[MessageHandler(Filters.location, do_done)]
    )
    return conv_handler
