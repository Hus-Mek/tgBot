import telebot
import urllib.request
import os
import praw 
import threading

bot_token = '835075644:AAERQCEPXSjpc-Z9SvZFPFcbPXNfiLUS3QI'
bot = telebot.TeleBot(token=bot_token)
reddit = praw.Reddit(client_id= 'D1O4NdmXoZVNpg', client_secret= 'voQJq4BVb4DWL8WMFCsmiZRzou4', username= 'tgdankbot', password= 'Kutaluta@3crest', user_agent= 'v1' )
sub1 = reddit.subreddit('dankmemes')
sub2 = reddit.subreddit('youngpeopleyoutube')
sub3 = reddit.subreddit('cursedcomments')
sub4 = reddit.subreddit('cursedimages')
hot_memes = sub1.top('day',limit=10)
hot_yout = sub2.top('day', limit=5)
hot_curcom = sub3.top('day',limit=5)
hot_curimg = sub4.top('day', limit=5)
url_arr = []



def update_urls():
    del url_arr[:]
    for submission in hot_memes:
        if not submission.stickied:
            url_arr.append(submission.url)
    for submission in hot_yout:
        if not submission.stickied:
            url_arr.append(submission.url)
    for submission in hot_curcom:
        if not submission.stickied:
           url_arr.append(submission.url)
    for submission in hot_curimg:
        if not submission.stickied:
           url_arr.append(submission.url)

def dl(url):
    f = open('pic.jpg', 'wb')
    f.write(urllib.request.urlopen(url).read())
    f.close

def send_photo(): 
    threading.Timer(88400,send_photo).start()
    update_urls()
    count = len(url_arr) 
    for i in range(0,count):
        dl(url_arr[i])
        img = open('pic.jpg','rb')
        bot.send_photo(chat_id ='@testingbottg',photo = img)
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
        
def listener(messages):
    for m in messages:
        print(str(m))


bot.set_update_listener(listener)
bot.polling()
