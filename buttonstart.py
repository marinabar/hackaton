import telebot
from telebot import types
import random

from telebot.types import InlineKeyboardMarkup

token = "856605416:AAFRXqkaK4KfowU_5mF_yGspny4iEOLKeqk"
# Обходим блокировку с помощью прокси
telebot.apihelper.proxy = {'https': 'socks5h://geek:socks@t.geekclass.ru:7777'}

bot = telebot.TeleBot(token=token)

# get the first line if this is the one with the words words
text= open("word_rus.txt", "rb").read().decode("utf-8")
lines = text.split()
o=random.randint(1,len(lines))
line = lines[o]
raspi={'8:30': random.choice(lines), '9:00': random.choice(lines), '10:00': random.choice(lines), '11:30': random.choice(lines),
       '12:00': random.choice(lines), '14:00': random.choice(lines), '15:00': random.choice(lines), '16:30': random.choice(lines),
       '17:00': random.choice(lines), '18:30': random.choice(lines), '19:00': random.choice(lines), '20:00': random.choice(lines),
       '22:00': random.choice(lines), '00:00': random.choice(lines)}


#raspi0=for key, val in raspi:
@bot.message_handler(commands=["start"])
def start(message):
    text = message.text
    user = message.chat.id

    markup = types.ReplyKeyboardMarkup()
    new = types.InlineKeyboardButton(text="→", callback_data='gener')
    markup.add(new)
    bot.send_message(user, text='generate', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def text_handler(message):
    user = message.chat.id
    if message.text=="→":
        markup1 = types.InlineKeyboardMarkup(row_width=2)
        for nom in raspi:
            button = types.InlineKeyboardButton(text= nom + ' ' + raspi[nom], callback_data=nom)
            markup1.add(button)
        bot.send_message(user, "choose", reply_markup=markup1)
    markup3 = types.ReplyKeyboardMarkup(row_width=2)
    ok = types.InlineKeyboardButton(text="Всё ок, давай в канал ☺", callback_data="ok")
    again = types.InlineKeyboardButton(text="Сгенерировать заново", callback_data="generagain")
    markup3.add(ok,again)
    bot.send_message(user, text='ツ', reply_markup=markup3)



# функция запустится, когда пользователь нажмет на кнопку
@bot.callback_query_handler(func=lambda call: True)
def callback_inline1(call):
    if call.message:
        if call.data == "generan":
            markup2 = types.InlineKeyboardMarkup(row_width=2)
            for nom in raspi:
                button1 = types.InlineKeyboardButton(text=nom + ' ' + raspi[nom], callback_data=nom)
                markup2.add(button1)
            bot.send_message(user, "choose what you wanna doo", reply_markup=markup1)

            markup.add(itembtn1, itembtn2)
        if call.data == "ok":
            pass


bot.polling(none_stop=True)