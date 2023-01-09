import random

def start():
    while True:
        n = random.randint(0, 1)
        if n == 0:
            bot.reply_to(message,'\nПервым будет ходить игрок!')
        else:
            bot.reply_to(message,'\nПервым будет ходить бот!')
        break
    return n

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

def step_bot(candy):
    n = candy % 29
    if n == 0:
        n = random.randint(1, 28)
    return n

def run_game():

    candy = 117
    count = 1
    up = start()
    while True:
        print(f'\n---------------- Ход номер: {count} ----------------')
        if up % 2 == 0:
            print(f'Ход игрока! Всего конфет: {candy}')
            n = step_pl(candy)
            print(f'Вы взяли: {n} конфет')
        elif up % 2 == 1:
            print(f'Ход бота! Всего конфет: {candy}')
            n = step_bot(candy)
            print(f'Бот взял: {n} конфет')
        candy -= n
        if candy == 0:
            if up % 2 == 0:
                winner = 'игрок'
            else:
                winner = 'бот'
            break
        up += 1
        count += 1
    return winner


