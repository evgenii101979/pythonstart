# Создать бота для вывода текущего курса валют(желательно запрос по конкретной валюте)
# currency USD

import telebot

bot = telebot.TeleBot('TOKEN')




print('сервер в работе')
bot.infinity_polling()
