# модуль для записи результатов вычислений

def log_exec(expr: str, result: str):
    """записывает в файл результат вычислений в виде задача -> ответ"""
    with open('history.csv', 'a') as h:
        h.write(f'\n{expr}; {result}')

def get_history() -> list[str]:
    """возвращает содержимое файла с результатами вычисления"""
    with open('history.csv', 'r') as h:
        return h.read()
