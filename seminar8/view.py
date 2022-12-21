# модуль для ввода\вывода информации

def choose() -> str:
    """выбор режима работы приложения
на вход ничего, на выход приложение"""
    print('1 - solve expression\n\
2 - solve equasion\n\
3 - simplify polinom\n\
4 - show history')
    return input('Choose mode: ')

def get_expr() -> str:
    """запрашивает у пользователя задачу"""
    return input('enter expression: ')

def show_res(res: str):
    """выводит результат"""
    print(res)

def error_mode():
    """ничего не принимает возвращает сообщение об ошибке выбора"""
    print('Такого режима нет')

def show_history(history: str):
    """выводит историю операций"""
    print(history.split('\n'))
    for i in history.split('\n'):
        print(i.replace(';', '-> результат: '))
