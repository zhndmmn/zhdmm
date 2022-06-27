import telebot
import random
from telebot import types
from pytube import YouTube
import flask
import os

# py -m pip install pytube

server = flask.Flask(__name__)

app_name = 'youtube-bot-downloader'
token = '5432678033:AAHXyWowK4GL1aeo1omm8M1L6RDtYTLi3tA'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, 'с тебя ссылка, с меня посылка')

@bot.message_handler(content_types=['text'])
def get_video(msg):
    link = msg.text
    video = YouTube(link)
    filename = video.streams.filter(res='720p').first().default_filename
    video.streams.filter(res='720p').first().download()
    file = open(filename, 'rb')
    bot.send_video(msg.chat.id, file)
    bot.send_message(msg.chat.id, 'Приятного просмотра')

@server.route('/' + token, methods=['POST'])
def get_message():
      bot.process_new_updates([types.Update.de_json(flask.request.stream.read().decode("utf-8"))])
      return "!", 200

@bot.message_handler(commands=['button'])
def button_message(msg):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Кнопка")
    markup.add(item1)
    bot.send_message(message.chat.id,'ну и зачем ты на это нажал',reply_markup=markup)
 @bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Кнопка":
        bot.send_message(message.chat.id,"мда кринж")
    
@server.route('/', methods=["GET"])
def index():
    print("hello webhook!")
    bot.remove_webhook()
    bot.set_webhook(url=f"https://{app_name}.herokuapp.com/{token}")
    return "Hello from Heroku!", 200


if __name__ == '__main__':
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
