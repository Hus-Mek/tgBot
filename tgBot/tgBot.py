import telebot
import urllib.request
import os
import praw 
import threading
from flask import Flask, request

bot_token = '835075644:AAEPAYlcnF9By_N9fuo8C4FlzOA5DyrfLr8'
bot = telebot.TeleBot(token=bot_token)
reddit = praw.Reddit(client_id= 'D1O4NdmXoZVNpg', client_secret= 'voQJq4BVb4DWL8WMFCsmiZRzou4', username= 'tgdankbot', password= 'Kutaluta@3crest', user_agent= 'v1' )
sub1 = reddit.subreddit('dankmemes')
sub2 = reddit.subreddit('youngpeopleyoutube')
sub3 = reddit.subreddit('cursedcomments')
sub4 = reddit.subreddit('cursedimages')
hot_memes = sub1.hot(limit=10)
hot_yout = sub2.hot(limit=7)
hot_curcom = sub3.hot(limit=7)
url_arr = []
server = Flask(__name__)



def update_urls():
    del url_arr[:]
    for submission in hot_memes:
        if not submission.stickied and 'jpg' in submission.url:
            url_arr.append(submission.url)
    for submission in hot_yout:
        if not submission.stickied and 'jpg' in submission.url:
            url_arr.append(submission.url)
    for submission in hot_curcom:
        if not submission.stickied and 'jpg' in submission.url:
           url_arr.append(submission.url)
    print(len(url_arr))

def dl(url):
    f = open('pic.jpg', 'wb')
    f.write(urllib.request.urlopen(url).read())
    f.close

def send_photo(): 
    threading.Timer(44000,send_photo).start()
    update_urls()
    count = len(url_arr) 
    for i in range(0,count-1):
        dl(url_arr[i])
        img = open('pic.jpg','rb')
        bot.send_photo(chat_id ='@memesandautism',photo = img)
        img.close



@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome, press /help for more information')

@bot.message_handler(commands = ['help'])
def send_welcome(message):
    bot.reply_to(message, 'Hit /send')

@bot.message_handler(func=lambda message: 'send 384252204' in message.text)
def every24(message):
        send_photo()
        
@server.route('/' + bot_token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://dankmemes-bot.herokuapp.com/' + bot_token)
    return "!", 200

if __name__ == "__name__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 8000)))
