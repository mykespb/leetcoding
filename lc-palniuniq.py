#!/usr/bin/env python

# Mikhail Kolodin
# lc-palinuniq.py 2023-06-09 2023-06-09 1.0

from itertools import permutations as func

def solve(s: str) -> list[str]:
    """make palins"""

    sl = list(s)
    res = set()

    for e in func(sl, len(sl)):
        # print(e)
        if ispalin(e):
            res |= {"".join(e)}

    return list(res)


def ispalin(s: str) -> bool:
    """check for palindrome"""

    return s == s[::-1]


def test(s: str):
    """print test results"""
    print(f"\ntask:   {s=}\nresult: {solve(s)}")

test("aabb")
test("abc")

# task:   s='aabb'
# result: ['baab', 'abba']

# task:   s='abc'
# result: []

# Палиндромная перестановка II

#  (https://leetcode.com/problems/palindrome-permutation-ii/)
# Сложность задачи: Средняя

# Условие задачи:
# Дана строка s. Требуется вернуть все ее палиндромные перестановки (без дубликатов).

# Вы можете вернуть ответ в любом порядке. Если s не имеет палиндромной перестановки, вернуть пустой список.

# Пример:
# Ввод: s = "aabb"
# Вывод: ["abba","baab"]

# Ввод: s = "abc"
# Вывод: []

# Решение задачи (https://telegra.ph/Reshenie-zadachi-08-12)
