import telebot
from telebot import types
from pytube import YouTube


t = '5432678033:AAHXyWowK4GL1aeo1omm8M1L6RDtYTLi3tA'
bot = telebot.TeleBot(t)
@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id,'cкинь ссылку')
@bot.message_handler(content_types=['text'])
def get_video(msg):
    link = msg.text
    video = YouTube(link)
    filename = video.streams.filter(res='720p').first().default_filename
    video.streams.filter(res='720p').first().download()
    file = open(filename,'rb')
    bot.send_video(msg.chat.id, file)
    bot.send_message(msg.chat.id,'приятного')


    print('done')

bot.polling()
    
