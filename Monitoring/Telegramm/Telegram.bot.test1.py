import telebot
import requests
from time import sleep as sleep
#Token
TOKEN = '328879011:AAFG6IuyOG9LhzzhpoEJPXyqnkiLw1lQQbk'
#Bot
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Как тебя зовут?')
    bot.register_next_step_handler(sent, hello)
def hello(message):
    bot.send_message(
        message.chat.id,
        'Привет, {name}. Рад тебя видеть.'.format(name=message.text))


@bot.message_handler(commands=['pogoda'])
def pogoda(message):
    r = requests.get('https://api.openweathermap.org/data/2.5/forecast?id=5202009&APPID=aa381018a37124f8582d2d52560ea692')
    temp = ((r.json())['list'][0])['main']['temp'] - 273
    temp = str(round(temp, 2))
    temp = "Температура в Москве " + temp + "С"
    bot.send_message(message.chat.id, temp)

@bot.message_handler(commands=['help'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Как тебя зовут?')
    bot.register_next_step_handler(sent, hullo)

def hullo(message):
    bot.send_message(
        message.chat.id,
        'Мммм.....'.format(name=message.text))
    sleep(1)
    bot.send_message(
        message.chat.id,
        'Убейся, {name}.'.format(name=message.text))

bot.polling()