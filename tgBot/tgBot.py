import telebot
import urllib.request
import os
from flask import Flask

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
    #bot.send_chat_action(message.chat.id, 'upload photo')
    img = open('pic.jpg','rb')
    bot.send_photo(message.chat.id,img, reply_to_message_id=message.message_id)
    img.close
def listener(messages):
    for m in messages:
        print(str(m))


bot.set_update_listener(listener)
bot.polling()