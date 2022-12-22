
def choose_mode():
    print('Введите цифру 1 если хотите играть "117 конфет"')
    print('Введите цифру 2 если хотите играть "крестики-нолики"')
    return input()

def show_results(winner):
    if winner == 'игрок':
        print('\nПобедил игрок')
    else:
        print('\nПобедил бот')