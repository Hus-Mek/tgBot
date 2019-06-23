import telebot
import urllib.request
import os
import praw 

bot_token = '835075644:AAERQCEPXSjpc-Z9SvZFPFcbPXNfiLUS3QI'
bot = telebot.TeleBot(token=bot_token)
reddit = praw.Reddit(client_id= 'D1O4NdmXoZVNpg', client_secret= 'voQJq4BVb4DWL8WMFCsmiZRzou4', username= 'tgdankbot', password= 'Kutaluta@3crest', user_agent= 'v1' )
subreddit = reddit.subreddit('dankmemes')
hot_memes = subreddit.top('day', limit=20)
url_arr = []



def update_urls():
    for submission in hot_memes:
        if not submission.stickied:
            url_arr.append(submission.url)


def dl(url):
    f = open('pic.jpg', 'wb')
    f.write(urllib.request.urlopen(url).read())
    f.close



@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome, press /help for more information')

@bot.message_handler(commands = ['help'])
def send_welcome(message):
    bot.reply_to(message, 'Hit /send')

@bot.message_handler(commands = ['send'])
def send_photo(message): 
    update_urls()
    for i in range(0,20):
     dl(url_arr[i])
     img = open('pic.jpg','rb')
     bot.send_photo(message.chat.id,img, reply_to_message_id=message.message_id)
     img.close

def listener(messages):
    for m in messages:
        print(str(m))


bot.set_update_listener(listener)
bot.polling()
