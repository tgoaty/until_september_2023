import telebot
import datetime
from random import*
"""Katya popa"""
token = '5338859589:AAGsz1XHv-3qYKeSphgTwVEDtnyQOLE-X28'
bot = telebot.TeleBot(token)
file = 'debug log.txt'

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'status:online' )

@bot.message_handler(content_types=["text"])
def new_message(message):
    mess = message.text
    dt_now = str(datetime.datetime.now())
    nf = str(randint(1, 217))
    mes = mess + ' ' + dt_now[:-7] + ' ' + nf
    with open(file, 'a') as debug_log:
        debug_log.write('\n')
        debug_log.write(mes)
    debug_log.close()
    print(mes)

    #"U\16\A.png"
    #"S\2.jpg"
    photo = mess[0].upper() + '\\' + mess[1:-1] + '\\' + mess[-1].upper() + '.png'
    photo2 = 'S' + '\\' + nf + '.jpg'
    try:
        img = open(photo, 'rb')
        img2 = open(photo2, 'rb')
        bot.send_photo(message.chat.id, img)
        bot.send_photo(message.chat.id, img2)
    except FileNotFoundError:
        bot.send_message(message.chat.id, 'Это упражнение пока не добавлено')


bot.infinity_polling()
