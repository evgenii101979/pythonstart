import telebot
import random
from random import choice

bot = telebot.TeleBot('TOKEN')

print('сервер в работе')

candy = dict()
st_game = dict()
turn = dict()


def game_proc(message):
    global st_game
    try:
        if st_game[message] and 1 <= int(message.text) <= 28:
            return True
        else:
            return False
    except KeyError:
        st_game[message] = False
        if st_game[message] and 1 <= int(message.text) <= 28:
            return True
        else:
            return False

@bot.message_handler(commands=['game'])
def new_game(message):
	bot.reply_to(message, '\n-------- Игра "117 конфет" -----------\
							нажмите /start, для выбора очередности и начала игры\n')

@bot.message_handler(commands=['start'])
def start(message):
    global candy, turn
    candy[message] = 117
    turn = random.randint(0, 1)
    if turn == 0:
        bot.reply_to(message, f'первым начинает игрок!\nна столе {candy[message]} конфет, сколько вы возьмете?')
    else:
        step_bot = random.randint(1, candy[message] % 29)
        candy[message] -= step_bot
        bot.reply_to(message, f'первым начинает бот!\n бот взял {step_bot} конфет. осталось {candy[message]} конфет')

@bot.message_handler(func=game_proc)
def proc(message):
    global turn, candy, st_game
    if turn == 0:
        if candy[message] > 28:
            candy[message] -= int(message.text)
            bot.send_message
            (message, f'вы взяли {message.text} осталось {candy[message]} конфет')
            if candy[message] > 28:
                step_bot = random.randint(1, candy[message] % 29)
                candy[message] -= step_bot
                bot.send_message(message, f'Бот взял {step_bot} конфет')
                bot.send_message(message, f'Осталось {candy[message]} конфет')
                if candy[message] <= 28:
                    bot.send_message(message, 'User Win')
                    st_game[message] = False
            else:
                bot.send_message(message, 'Bot Win')
                st_game[message] = False
        else:
            bot.send_message(message, 'Bot Win')
            st_game[message] = False

bot.infinity_polling()