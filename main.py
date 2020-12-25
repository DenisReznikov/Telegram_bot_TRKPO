from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, ConversationHandler, CallbackQueryHandler, MessageHandler,Filters
import scr.handlers.handler_eat as eat
import scr.handlers.handler_weather as weather
import scr.handlers.avito_handler as avito
import scr.other.state as s



def do_start(update: Update, context):
    # TODO: перенести клавву в другой класс
    location_keyboard = [[KeyboardButton("Send location", request_location=True), ], ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=location_keyboard,
        resize_keyboard=True,
    )

    answer = "Привет, " + update.message.from_user.first_name + "." + \
             "\nЯ твой помощник." \
             "\n\nЕсли вы хотите пить или есть, нажмите -> /eat \n\n" \
             "Чтобы посмотреть погоду - /weather \n\n" \
             "Или если вы хотите я могу найти что-то на Авито, нажмите - /avito"

    update.message.reply_text(text=answer, reply_markup=keyboard)
    return s.ALL_FIRST_COMMAND

def do_end(update: Update, context :  CallbackContext):

    answer = "Пока, " + update.message.from_user.first_name + ".\n" + \
             "Нажми /start что бы заново меня вызвать"
    update.message.reply_text(text=answer)
    return  ConversationHandler.END



def main():



    main_conversation = ConversationHandler(
        entry_points=[CommandHandler("start", do_start)],
        states={
            s.ALL_FIRST_COMMAND: [
                CommandHandler('avito', avito.do_avito),
                CommandHandler('eat', eat.do_eat),
                CommandHandler('weather', weather.do_start_weather),
                CommandHandler("end", do_end)
            ],
            s.AVITO_METRO: [CommandHandler("end", do_end),MessageHandler(Filters.text, avito.add_metro)],
            s.AVITO_TYPE_SORT:[CommandHandler("end", do_end),MessageHandler(Filters.text, avito.choose_type_sort)],
            s.AVITO_FINAL:[CommandHandler("end", do_end),CallbackQueryHandler(avito.send_result)],
            s.LOC_WEATHER:[CommandHandler("end", do_end),MessageHandler(Filters.location,weather.do_location),
                       MessageHandler(Filters.text, weather.do_city)],
            s.RESULT_WEATHER:[CommandHandler("end", do_end),CallbackQueryHandler(weather.do_done)],
            s.CHOOSING_EAT: [CommandHandler("end", do_end),CallbackQueryHandler(eat.button)],
            s.RESULT_EAT: [CommandHandler("end", do_end),MessageHandler(Filters.location, eat.do_done)]
        },
        fallbacks=[CommandHandler("end", do_end)]
    )
    updater = Updater("1486083484:AAEBHCVAtKRQRD0neNbem7NgrUAnbIo2enU", use_context=True)
    dispatcher = updater.dispatcher




    dispatcher.add_handler(main_conversation)

    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    main()
