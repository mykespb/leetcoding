#!/usr/bin/env python

# Mikhail Kolodin
# lc-maxprefix.py 2023-06-15 2023-06-15 1.0

def solve(arr: list[str]) -> str:
    """find longest prefix for array of strings"""

    if len(arr) == 0:
        return ''
    
    mlen = min(len(s) for s in arr)

    for tlen in range(mlen, 1, -1):
        for e in arr:
            if e[:tlen] != arr[0][:tlen]:
                break
        else:
            return e[:tlen]
        
    return ''


def test(arr: list[str]):
    """print test results"""

    print(f'task: {arr=},\nresult: "{solve(arr)}"')

test(["flower", "flow", "flight"])
test(["dog", "racecar", "car"])

# task: arr=['flower', 'flow', 'flight'],
# result: "fl"
# task: arr=['dog', 'racecar', 'car'],
# result: ""

# Наибольший общий префикс

# Частота встречи задач на собеседованиях за последние шесть месяцев:
# Facebook* — 21, Amazon — 16, Apple — 14, Adobe — 11, Google — 9, Microsoft — 6, Uber — 6.

# Условие задачи:
# Напишите функцию для поиска самого длинного общего префикса у массива строк. Если общего префикса нет, верните пустую строку.

# Требуемая сложность:
# O(S), S — сумма всех символов во всех строках.

# Примеры:
# Ввод: strs = ["flower","flow","flight"]
# Вывод: "fl"

# Ввод: strs = ["dog","racecar","car"]
# Вывод: ""
# Среди введенных строк нет общего префикса.

# Решение задачи

#  (https://telegra.ph/Reshenie-07-08-5)* — организация, признанная экстремистской на территории РФ.
