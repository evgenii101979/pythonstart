import telebot
# from main117 import start
# from main117 import step_pl
# from main117 import step_bot
# from main117 import process
import random


bot = telebot.TeleBot()

print('сервер в работе')

@bot.message_handler(commands=['game'])
def new_game(message):
	bot.reply_to(message, '\n-------- Игра "117 конфет" -----------\
							нажмите /start, для выбора очередностьи и начала игры\n')

@bot.message_handler(commands=['start'])

# def proc (message):
#     while True:
#         if up % 2 == 0:
#             bot.reply_to(message, 'Ход игрока! Всего конфет: {candy}')
#             n = step_pl(candy)
#             bot.reply_to(message, f'Вы взяли: {n} конфет')
#         elif up % 2 == 1:
#             print(f'Ход бота! Всего конфет: {candy}')
#             n = step_bot(candy)
#             print(f'Бот взял: {n} конфет')
#         candy -= n
#         if candy == 0:
#             if up % 2 == 0:
#                 bot.reply_to(message, 'Победил игрок!')
#             else:
#                 bot.reply_to(message,'Победил бот!')
#             break
#         up += 1
#         count += 1
#     return winner

def step_pl(candy):
    n = 29
    while n > 28 or n < 1:
        n = input('сколько конфет вы берете? ')
        if n.isdigit():
            n = int(n)
            if n > 28 or n < 1:
                print('столько брать нельзя! Возьмите от 1 до 28')
            if n > candy:
                print('столько конфет нет!')
                n = 29
        else:
            print('Вы ввели недопустимые символы. Введите число от 1 до 28')
            n = 29
    return n
# def step_pl(message):
# 	while can > 28 or can < 1:
# 		can = int(message.text)
# 		bot.reply_to(message, f'\nвы взяли {can} конфет')
# 		bot.reply_to(message, f'\nна столе осталось {candy -can} конфет, ход бота')
# 		if can > 28 or can < 1:
# 			bot.reply_to(message,'столько брать нельзя! Возьмите от 1 до 28')
# 		if can > candy:
# 			bot.reply_to(message,'столько конфет нет!')
# 			can = 29
# 	else:
# 		bot.reply_to(message,'Вы ввели недопустимые символы. Введите число от 1 до 28')
# 		can = 29

def turn(message):
	candy = 117
	count = 1
	select = random.randint(0, 1)
	if select == 0:
		bot.reply_to(message, '\nПервым будет ходить игрок!')
		if candy > 28:
            can -= int(message.text)
			bot.reply_to(message, f'вы взяли {can} конфет')
            bot.reply_to(message, f'Осталось {candy}')
		else:
			
	else:
		bot.reply_to(message, '\nПервым будет ходить бот!')
		can = random.randint(1, candy % 29)
		bot.reply_to(message, f'\n---------------- Ход номер: {count} ----------------')
		
		bot.reply_to(message, f'\nбот взял {can} конфет')
		bot.reply_to(message, f'\nна столе осталось {candy -can} конфет, ваш ход')
	count += 1

def st_game(message):
    bot.reply_to(func=turn)




# @bot.proc(func=turn)
# def step_pl(candy):
#     n = 29
#     while n > 28 or n < 1:
#         n = input('сколько конфет вы берете? ')
#         if n.isdigit():
#             n = int(n)
#             if n > 28 or n < 1:
#                 print('столько брать нельзя! Возьмите от 1 до 28')
#             if n > candy:
#                 print('столько конфет нет!')
#                 n = 29
#         else:
#             print('Вы ввели недопустимые символы. Введите число от 1 до 28')
#             n = 29
#     return n

def step_bot(candy):
    n = candy % 29
    if n == 0:
        n = random.randint(1, 28)
    return n

bot.infinity_polling()