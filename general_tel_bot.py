from datetime import datetime
from telegram import update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
from telegram.utils.request import Request


#mybot = Updater("2039097737:AAEVO2f5St1OS3q0BuE0e4iEEnmp4wTblzY", use_context=True)

#PROXY = {'proxy_url': utilits.PROXY_URL,
    #'urllib3_proxy_kwargs': {
        #'username': utilits.PROXY_USERNAME,
        #'password': utilits.PROXY_PASSWORD
    #}
#}

def greet_user(update, context):
    print("Вызван /start")
    update.message.reply_text("Здравствуй, пользователь!")  

def check_connectin(update, context):
    print("Отправляем запрос во Falsk")
    resp = requests.post(url='https://1201-84-253-126-202.ngrok.io')
    print(resp.text)
    update.message.reply_text(resp.text)


def talk_to_me(update, context):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater("2039097737:AAEVO2f5St1OS3q0BuE0e4iEEnmp4wTblzY", use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("Learn", greet_user))
    dp.add_handler(CommandHandler("Check", check_connectin))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()



if __name__ == "__main__":
    main()
    