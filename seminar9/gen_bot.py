import telebot
import model_del_abc

bot = telebot.TeleBot('TOKEN')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, model_del_abc.abc_delete(message.text))

print('сервер в работе')
bot.infinity_polling()






