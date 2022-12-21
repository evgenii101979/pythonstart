# модуль для выполнения операции
import sympy

def execute_expr(expr: str) -> str:        # (3+4)*10=70
    """принимает на вход строку пример.возвращает результат примера"""
    return str(eval(expr))

def solve_eq(expr: str) -> str:        # x**3 - 8 = 0 -> 2 \\ x**2 -1 = 0 -> [1, -1]
    """принимает на вход уравнение в виде строки и возвращает список корней уравнения
    в строку с разделителем"""
    try:
        x = sympy.Symbol('x')
        res = sympy.solve(expr, x)
        res = list(map(str, res))
        return " || ".join(res)
    except ValueError:
        return 'Incorrect input'

def simpify_pol(expr: str) -> str:      # x**2+3*x**2+4 -> 
    """упрощает введенный многочлен"""
    pass