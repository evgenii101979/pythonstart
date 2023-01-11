# Создать бота для вывода текущего курса валют(желательно запрос по конкретной валюте)
# currency USD

import requests
import telebot
from telebot import types

bot = telebot.TeleBot('5801925811:AAHcFjH5GqaOLZnxl8aSBxn1JnJWjb13PCM')
print('сервер в работе')

@bot.message_handler(commands=['currency'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width = 2, resize_keyboard=True, )
    usd = types.KeyboardButton('USD')
    eur = types.KeyboardButton('EUR')
    gbp = types.KeyboardButton('GBP')
    byn = types.KeyboardButton('BYN')
    markup.add(usd, eur, gbp, byn)
    bot.send_message(message.chat.id, 'выберите валюту', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    if message.text == 'USD':
        dol = res['Valute']["USD"]['Name']
        dol2 = res['Valute']["USD"]['Value']
        bot.send_message(message.chat.id, f'курс {dol} {dol2}')
    elif message.text == 'EUR':
        evro = res['Valute']["EUR"]['Name']
        evro2 = res['Valute']["EUR"]['Value']
        bot.send_message(message.chat.id, f'курс {evro} {evro2}')
    elif message.text == 'GBP':
        funt = res['Valute']["GBP"]['Name']
        funt2 = res['Valute']["GBP"]['Value']
        bot.send_message(message.chat.id, f'курс {funt} {funt2}')
    elif message.text == 'BYN':
        bel_rub = res['Valute']["BYN"]['Name']
        bel_rub2 = res['Valute']["BYN"]['Value']
        bot.send_message(message.chat.id, f'курс {bel_rub} {bel_rub2}')
    
bot.infinity_polling()
