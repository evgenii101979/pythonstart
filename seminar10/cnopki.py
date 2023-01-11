import telebot
from telebot import types

bot = telebot.TeleBot()

@bot.message_handler(commands=["start"])
def start_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    Catalog = types.KeyboardButton(text="Каталог")
    Info = types.KeyboardButton(text="Инофрмация")
    keyboard.add(Catalog, Info)
    return keyboard

# @bot.message_handler(content_types=['text'])
# def catalog_keyboard():
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     Steam = types.KeyboardButton(text="Steam")
#     Origin = types.KeyboardButton(text="Origin")
#     UPlay = types.KeyboardButton(text="UPlay")
#     EpicGames = types.KeyboardButton(text="Epic Games")
#     VPN = types.KeyboardButton(text="VPN")
#     keyboard.add(Steam, Origin, UPlay, EpicGames, VPN)
#     return keyboard


bot.infinity_polling()