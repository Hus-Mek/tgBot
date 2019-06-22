import telebot
import urllib.request
import os
from flask import Flask

bot_token = '835075644:AAERQCEPXSjpc-Z9SvZFPFcbPXNfiLUS3QI'
bot = telebot.TeleBot(token=bot_token)
server = Flask(_name_)

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

@server.route('/' + bot_token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=' https://botttg.herokuapp.com/' + bot_token)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))