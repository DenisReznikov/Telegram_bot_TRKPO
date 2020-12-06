from telegram import Update
from telegram.ext import (CommandHandler, MessageHandler, Filters,
                          ConversationHandler, CallbackQueryHandler, CallbackContext)



def eat_handler():
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('eat', do_eat)],
        states={CHOOSING: [CallbackQueryHandler(button)]},
        fallbacks=[MessageHandler(Filters.location, do_done)]
    )
    return conv_handler