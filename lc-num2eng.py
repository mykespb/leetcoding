#!/usr/bin/env python

# Mikhail Kolodin
# lc-num2eng.py 2023-06-22 2023-06-22 1.0

from string import capwords

klasses = ["", "thousand", "million", "billion"]  # etc

smalls = {
    0: "",
    1: "one", 
    2: "two", 
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

decs = {
    2: "twenty",
    3: "thirty",
    4: "fourty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}

def say(num: int) -> str:
    """say it in English"""

    if num == 0:
        return "Zero"
    
    res = ""
    klass = 0

    while num:
        sub = num % 1000
        num //= 1000

        res = subsay(sub, klass) + " " + res
        klass +=1

    return capwords(res)

def subsay(num: int, klass:int) -> str:
    """give subresult for 1 klass (0..999) + say its klass name"""

    resnum = saynum(num)
    resklass = sayklass(num, klass)

    return resnum + " " + resklass

def saynum(num: int) -> str:
    """say 1 klass value"""

    res = sayhund(num // 100)
    res = res + saydec(num % 100)

    return res

def saydec(d: int) -> str:
    """say 10..99"""

    if d < 20:
        return smalls[d]

    return decs[d//10] + " " + smalls[d%10]

def sayhund(h: int) -> str:
    """say hundreds"""

    if h == 0:
        return ""
    if h == 1:
        return " one hundred "
    return smalls[h] + " hundreds "

def sayklass(num: int, klass: int) -> str:
    """say 1 klass name"""

    if klass == 0:
        return ""
    if num % 10 == 1 and (num%100 < 10 or num%100 > 20):
        return klasses[klass]
    return klasses[klass] + "s"

def test(num: int) -> None:
    """print test results"""

    print(f'task: {num}, result: {say(num)}')

# test(0)
test(123)
test(12345)

# task: 123, result: One Hundred Twenty Three
# task: 12345, result: Twelve Thousands Three Hundreds Fourty Five

# Целое число английскими словами

#  (https://leetcode.com/problems/integer-to-english-words/)Сложность задачи: Трудная

# Условие задачи:
# Преобразуйте неотрицательное целое число num в его представление английскими словами.

# Пример:
# Ввод: num = 123
# Вывод: "One Hundred Twenty Three"

# Ввод: num = 12345
# Вывод: "Twelve Thousand Three Hundred Forty Five"
