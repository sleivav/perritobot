import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import Updater

from reddit import get_random_post

load_dotenv()

PERRITO_BOT_TOKEN = os.getenv('PERRITO_BOT_TOKEN')
MIN_SCORE = 100

def perrito(update: Update, _: CallbackContext):
    post = get_random_post()
    while post['score'] < MIN_SCORE or post['post_hint'] != 'image':
        post = get_random_post()
    photo = post['url_overridden_by_dest']
    update.message.reply_photo(photo=photo)

def wisdom(update: Update, _: CallbackContext):
    update.message.reply_text('https://www.youtube.com/watch?v=D-UmfqFjpl0')

def main():
    updater = Updater(PERRITO_BOT_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("perrito", perrito))
    dispatcher.add_handler(CommandHandler("wisdom", wisdom))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
