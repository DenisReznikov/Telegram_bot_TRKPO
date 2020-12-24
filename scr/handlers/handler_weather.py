from telegram import Update
from telegram.ext import (CommandHandler, MessageHandler, Filters,
                          ConversationHandler, CallbackQueryHandler)
from scr.model.api_for_weather import request_current_weather, request_forecast
from scr.other.keyboard import get_yes_keyboard
from scr.other.logger import debug_requests

LOCATION, CITY = range(2)


@debug_requests
def do_start_weather(update: Update, context):
    update.message.reply_text(
        text="Send name of city or u location"
    )
    return LOCATION



@debug_requests
def do_location(update: Update, context):
    longitude, latitude = update.message.location.longitude, update.message.location.latitude
    context.user_data['city'] = ''
    context.user_data['longitude'] = longitude
    context.user_data['latitude'] = latitude
    answer = request_current_weather(lon=longitude, lat=latitude)
    update.message.reply_text(text=answer,
                              reply_markup=get_yes_keyboard())


@debug_requests
def do_city(update: Update, context):
    city = update.message.text
    context.user_data['city'] = city
    answer = request_current_weather(city_name=city)
    update.message.reply_text(text=answer)
    update.message.reply_text(text="Do you want to know weather in " + context.user_data.get('city') + " more DETAIL",
                              reply_markup=get_yes_keyboard())


@debug_requests
def do_done(update: Update, context):
    chat_id = update.effective_message.chat_id
    if update.callback_query.data == 'Yes':
        if context.user_data.get('city') == '' or context.user_data.get('city') is None:
            answer = request_forecast(lon=context.user_data['longitude'],
                                      lat=context.user_data['latitude'])
            context.bot.send_message(chat_id=chat_id, text=answer)
        else:
            answer = request_forecast(city_name=context.user_data.get('city'))
            context.bot.send_message(chat_id=chat_id, text=answer)
    else:
        context.bot.send_message(chat_id=chat_id, text="Okay. Bay")

    context.user_data.clear()
    return ConversationHandler.END


def weather_handler():
    conv_handler = ConversationHandler(
        entry_points=
        [
            CommandHandler('weather', do_start_weather)
        ],
        states=
        {
            LOCATION: [MessageHandler(Filters.location, do_location),
                       MessageHandler(Filters.text, do_city)]
        },
        fallbacks=[CallbackQueryHandler(do_done)]
    )
    return conv_handler
