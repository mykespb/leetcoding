#!/usr/bin/env python

# Mikhail Kolodin
# lc-telecomb.py 2023-06-19 2023-06-19 1.0

from itertools import product

def solve(nums: str) -> list[str]:
    """find longest prefix for array of strings"""

    tele = {"1": " ", 
        "2": "abc",
        "3": "def", 
        "4": "ghi",
        "5": "jkl", 
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
        "0": " "}

    seq = []
    for e in nums:
        seq += [ tele[e] ]
        # seq += [ list(tele[e]) ]

    # return seq
    return list(product(*seq))


def test(nums: str):
    """print test results"""

    print(f'task: "{nums}",\nresult:', end=" ")
    res = solve(nums)
    for r in res:
        print('"', "".join(r) .replace(" ", ""), '"', sep="", end=", ")

    print()

test("23")
test("123")
test("")

# task: "23",
# result: "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf", 
# task: "123",
# result: "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf", 
# task: "",
# result: "", 

# Буквенные комбинации номера телефона

# Получив строку, содержащую цифры от 2 до 9 включительно, вернуть все возможные комбинации букв, которые может представлять число. Верните ответ в любом порядке. Отображение цифр в буквы (точно так же, как на телефонных кнопках) приведено на картинке. Обратите внимание, что 1 не соответствует ни одной букве.

# Примеры:
# Ввод: nums = "23" 
# Вывод: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

# Ввод: digits = ""
# Вывод: []

# Ввод: digits = "2"
# Вывод: ["a","b","c"]

# Решение задачи (https://telegra.ph/Reshenie-zadachi-07-19)
