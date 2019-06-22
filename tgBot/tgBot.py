import telebot
import time
import urllib.request
from PIL import Image
import requests
from io import BytesIO


bot_token = '835075644:AAERQCEPXSjpc-Z9SvZFPFcbPXNfiLUS3QI'
bot = telebot.TeleBot(token=bot_token)


def dl(url):
    f = open('pic.jpg', 'wb')
    f.write(urllib.request.urlopen(url).read())
    f.close



@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome, press /help for more information')

@bot.message_handler(commands = ['help'])
def send_welcome(message):
    bot.reply_to(message, 'Send a url')

@bot.message_handler(func=lambda m: True)
def send_photo(message): 
    dl(message.text)
    bot.send_chat_action(message.chat.id, 'upload photo')
    img = open('pic.jpg','rb')
    bot.sendphoto(message.chat.id,img, reply_to_message_id=message.message_id)
    img.close

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)