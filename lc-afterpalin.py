#!/usr/bin/env python

# Mikhail Kolodin
# lc-afterpalin.py 2023-06-03 2023-06-03 1.0

from string import ascii_letters as letters

def ispalin(s: str) -> bool:
    """is s palin?"""

    s = [ c for c in list(s.lower()) if c in letters]
    return s == s[::-1]


def test(s: str):
    """show data and result"""

    print(f"""
          given string: {s}
          {'is a palindrome' if ispalin(s) else 'is not a palindrome'}
          """)


test("A man, a plan, a canal: Panama")
test("race a cat")
test("")


# Является ли строка палиндромом (https://leetcode.com/problems/valid-palindrome/)

# Сложность: Лёгкая

# Условие: палиндромом является фраза, которая после перевода в нижний регистр всех символов, а также удаления всех знаков препинания, читается одинаково как слева направо, так и справа налево. 

# Задача - вернуть true, если строка палиндром, false - в противном случае. 

# Пример:

# Ввод: s = "A man, a plan, a canal: Panama"
# Вывод: true
# Объяснение: "amanaplanacanalpanama" является палиндромом.

# Ввод: s = "race a car"
# Вывод: false
# Объяснение: "raceacar" не является палиндромом.

# Ввод: s = " "
# Вывод: true
# Объяснение: s - пустая строка "" после удаления всех знаков препинания и пробелов.
# Так как пустая строка читается одинаково в обоих направлениях, то она является палиндромом.

# Решение задачи (https://telegra.ph/YAvlyaetsya-li-stroka-palindromom-Reshenie-zadachi-08-14)
