#!/usr/bin/env python

# Mikhail Kolodin
# lc-longnorept.py 2023-07-07 2023-07-07 1.0

from collections import Counter

def norept(s: str) -> bool:
    """check if string has repetitions"""

    return all([ v<2 for k, v in Counter(s).items() ])


def solve(s: str) -> int:
    """solve it"""

    ml = 0
    for i1 in range(len(s) - 1):
        for i2 in range(i1+1, len(s)):
            if norept(s[i1:i2]) and i2-i1 > ml:
                ml = i2-i1
                # print(ml, s[i1:i2])
    return ml


def test(s: str) -> int:
    """run 1 test"""

    print(f"{s=} => {solve(s)}")

test("abcabcbb")
test("bbbbb")
test("pwwkew")

# s='abcabcbb' => 3
# s='bbbbb' => 1
# s='pwwkew' => 3


# Самая длинная подстрока без повторений

#  (https://leetcode.com/problems/longest-substring-without-repeating-characters/)
# Сложность: Средняя. 

# Условие задачи: дана строка надо найти самую длинную подстроку, в которой не будет повторений. 

# Пример:

# Ввод: s = "abcabcbb"
# Вывод: 3
# Объяснение: ответом является подстрока "abc", длина которой равна 3. 

# Ввод: s = "bbbbb"
# Вывод: 1

# Ввод: s = "pwwkew"
# Вывод: 3
# Объяснение: ответ - "wke" (длина = 3).
