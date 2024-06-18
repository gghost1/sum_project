import json

import requests
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
BOT_TOKEN = '6724137230:AAFVvHFvj7aWzDFyRNjh9gy2IShy2hHy2YM'

# Файл для хранения данных о каналах
CHANNELS_FILE = 'channels.json'



def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я ваш бот.')
def handle_channel_message(update: Update, context: CallbackContext) -> None:
    # Здесь вы обрабатываете сообщения, полученные из канала
    url = 'http://localhost:8080/addNews'
    post = {
        'message' : update.channel_post.text,
        'message_link' : update.channel_post.link,
        'chat_link' : update.effective_chat.link
    }
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.post(url, json=post, headers=headers)


def main() -> None:
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.chat_type.channel, handle_channel_message))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
