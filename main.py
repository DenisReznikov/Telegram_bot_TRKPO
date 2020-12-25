from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler
from scr.handlers.handler_eat import eat_handler
from scr.handlers.handler_weather import weather_handler
from scr.handlers.avito_handler import avito_handler
import os

def do_start(update: Update, context):
    # TODO: перенести клавву в другой класс
    location_keyboard = [[KeyboardButton("Send location", request_location=True), ], ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=location_keyboard,
        resize_keyboard=True,
    )

    answer = "Привет, " + update.message.from_user.first_name + " " + \
             "\n Я твой помощник." \
             "Если вы хотите пить или есть, нажмите -> /eat \n" \
             " \n"\
             "Чтобы посмотреть погоду - /weather \n" \
             "Или если вы хотите я могу найти что-то на Авито, нажмите - /avito" \

    update.message.reply_text(text=answer, reply_markup=keyboard)



def main():
    TOKEN =  ['TELEGRAM_TOKEN']
    updater = Updater("1486083484:AAEBHCVAtKRQRD0neNbem7NgrUAnbIo2enU", use_context=True)
    updater.dispatcher.add_handler(CommandHandler("start", do_start))
    updater.dispatcher.add_handler(eat_handler())
    updater.dispatcher.add_handler(weather_handler())
    updater.dispatcher.add_handler(avito_handler())
    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    main()
