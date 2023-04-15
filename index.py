from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext.updater import Updater
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.callbackqueryhandler import CallbackQueryHandler
from telegram.callbackquery import CallbackQuery
from telegram.ext.callbackcontext import CallbackContext
from telegram.update import Update
from telegram.message import Message
import sys
from time import sleep

# creating updater
updater: Updater = Updater("TOKEN",
                           use_context=True)
count=0

def error(update: Update, context: CallbackContext):
    """Log Errors caused by Updates."""
    sys.stderr.write("ERROR: '%s' caused by '%s'" % context.error, update)
    pass

def keyboards():
    keyboard = [[
        InlineKeyboardButton("Mathew", callback_data='Mathew'),
        InlineKeyboardButton("Mark", callback_data='Mark'),
     InlineKeyboardButton("Luke", callback_data='Luke'),
     InlineKeyboardButton("Luke", callback_data='John')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup

def start(update: Update, context: CallbackContext):
    """
    callback method handling /start command
    """


    reply_markup=keyboards()
    update.message.reply_text('Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Proin eget tortor risus. Donec rutrum congue leo eget malesuada.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Proin eget tortor risus.:', reply_markup=reply_markup)
    pass


def button(update, context):
    """
    callback method handling button press
    """
    global count

    query: CallbackQuery = update.callback_query
    query.answer()
    count+=1
    
    

    query.edit_message_text(text="Selected option: {}".format(query.data))
    reply_markup=keyboards()
    sleep(4)
    query.edit_message_text('Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Proin eget tortor risus. Donec rutrum congue leo eget malesuada.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Proin eget tortor risus.:\n ** your score:-'+str(count)+"**", reply_markup=reply_markup)
   
    


# adding listeners
updater.dispatcher.add_handler(CommandHandler('start', start))  # handling /start command
updater.dispatcher.add_handler(CallbackQueryHandler(button))  # handling inline buttons pressing
updater.dispatcher.add_error_handler(error)  # error handling

# started polling
updater.start_polling()