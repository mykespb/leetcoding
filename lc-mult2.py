#!/usr/bin/env python

# Mikhail Kolodin
# lc-mult2.py 2023-07-01 2023-07-01 1.0

def mult2(num1: str, num2: str) -> str:
    """multiply 2 integers, given as strings, and return it as a string"""

    n1 = gorn(num1)
    n2 = gorn(num2)
    prod = n1 * n2
    res = degorn(prod)
    return res


def gorn(num: str) -> int:
    """make int from string, decimal"""

    ord0 = ord('0')

    res = 0
    for c in num:
        res = res*10 + (ord(c) - ord0)

    return res


def degorn(num: int) -> str:
    """convert int to str"""

    ous= ""
    ord0 = ord('0')

    while num:
        dig = num % 10
        ous = chr(dig + ord0) + ous
        num //= 10

    return ous


def test(num1: str, num2: str) -> None:
    """print test results"""

    print(f"task: {num1=}, {num2=}, result: '{mult2(num1, num2)}'")

test("2", "3")
test("123", "456")

# task: num1='2', num2='3', result: '6'
# task: num1='123', num2='456', result: '56088'

# Умножение строк

#  (https://leetcode.com/problems/multiply-strings/)Сложность задачи: Средняя

# Условие задачи:
# Даны два неотрицательных целых числа num1 и num2, представленные в виде строк, вернуть произведение num1 и num2, также представленное в виде строки.

# Примечание. Вы не должны использовать какую-либо встроенную библиотеку BigInteger или напрямую преобразовывать входные данные в целое число.

# Пример:
# Ввод: num1 = "2", num2 = "3"
# Вывод: "6"

# Ввод: num1 = "123", num2 = "456"
# Вывод: "56088"
