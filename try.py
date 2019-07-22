import datetime
import telebot
from telebot import types
#from mongodata import *

token = "780552474:AAHkY4npvjJTwwByDxT5uEFRh1bedF4IBQ4"

telebot.apihelper.proxy = {'https': 'socks5h://geek:socks@t.geekclass.ru:7777'}

bot = telebot.TeleBot(token=token)


@bot.message_handler(commands=["start"])
def start(message):
    text = message.text
    user = message.chat.id
    bot.send_message(user, "Добро пожаловать!")
    keyboard = types.InlineKeyboardMarkup()
    #all_ = get_data()
    #current = all_[-1]
    #print(current)
    #print('mongo ok')
    ''''buttons = []
    for e in current['timetable']:
        buttons.append("%s %s" % (e['time'], e['text']))
        wake = types.InlineKeyboardButton("%s %s" % (e['time'], e['text']), callback_data='start')
        keyboard.add(wake)'''''

    done = types.KeyboardButton(text="ГОТОВО", callback_data='do_it')
    new = types.KeyboardButton(text="НОВОЕ РАСПИСАНИЕ", callback_data='new_ras')
    keyboard.add(new, done)
    bot.send_message(user, "Расписание на завтра:", reply_markup=keyboard)

# {'action': 'more', 'item': e}
@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    keyboard = types.InlineKeyboardMarkup()
    if call.data == 'start':
        chantime = types.InlineKeyboardButton(text="Изменить время", callback_data='time')
        creaname = types.InlineKeyboardButton(text="Ввести название", calback_data='name')
        backtoras = types.InlineKeyboardButton(text='Назад', calback_data='back')
        keyboard.add(creaname, chantime, backtoras)
    # if call.data == 'do_it':
    # if call.data == 'new_ras':
    if call.data == 'time':
        # Ввести своё(нужно доделать)
        more = types.InlineKeyboardButton(text='Больше', calback_data='more')
        less = types.InlineKeyboardButton(text='Меньше', calback_data='less')
        backtost = types.InlineKeyboardButton(text='Назад', calback_data='back')
        keyboard.add(more, less, backtost)
    if call.data == 'name':
        gener = types.InlineKeyboardButton(text='НОВАЯ СТРОКА', calback_data='stroke')
        # Ввести своё(нужно доделать)
        backtost = types.InlineKeyboardButton(text='Назад', calback_data='back')
        keyboard.add(gener, backtost)
    if call.data == 'more':
        pass


bot.polling(none_stop=True)