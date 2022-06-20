import telebot
from googletrans import Translator
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
    
'''
lang = ' '


@bot.message_handler(commands=['start'])
def start(message):
    k=types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    b1 = types.KeyboardButton('en')
    b2 = types.KeyboardButton('fr')
    k.add(b1, b2)
    bot.send_message(message.chat.id,'привет, выбери язык', reply_markup=k)
    

@bot.message_handler(content_types=['text'])
def answer(message):
	global lang
	if message.text ==  'en':
		lang = 'en'
		bot.reply_to(message,'введи текст, который нужно перевести ')
	if message.text ==  'fr':
		lang = 'fr'
		bot.reply_to(message,'введи текст, который нужно перевести ')
	bot.register_next_step_handler(message, ai)

def ai(message):
    translartor = Translator()
    text = translartor.translate(message.text, dest=lang)
    bot.send_message(message.chat.id, text.text)

       
bot.polling()
'''
