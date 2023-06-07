#!/usr/bin/env python

# Mikhail Kolodin
# lc-allana.py 2023-06-08 2023-06-08 1.0

from itertools import permutations as perm

def ana(s: str, p: str) -> list[int]:
    """count all anagrams"""
    
    if s == '' or p == '':
        return []
    
    res = set()
    ls = len(s)
    lp = len(p)

    for start in range(ls-lp+1):
        for test in perm(p):
            if s[start: start+lp] == "".join(test):
                res |= {start}

    return sorted(list(res))


def test(s, p):
    """ show """
    print(f"{s=}, {p=} -> {ana(s, p)}")


test('cbaababacd', 'abc')
test('abab', 'ab')


# s='cbaababacd', p='abc' -> [0, 6]
# s='abab', p='ab' -> [0, 1, 2]

# Нахождение всех анаграмм в строке

#  (https://leetcode.com/problems/find-all-anagrams-in-a-string/)Сложность: Средняя

# Условие задачи: даны две строки s и p, надо вернуть все индексы стартовых позиций, с которых начинаются анаграммы внутри строки s. 

# Анаграмма - строка, составленная путём перестановок букв из какого либо базового набора. 

# Пример: 

# Ввод: s = "cbaebabacd", p = "abc"
# Вывод: [0,6]

# Объяснение:
# Подстрока  "cba" начинается с индекса 0, она является анаграммой строки "abc".
# Подстрока  "bac" начинается с индекса 6, она является анаграммой строки "abc".

# Ввод: s = "abab", p = "ab"
# Вывод: [0,1,2]

# Решение задачи (https://telegra.ph/Nahozhdenie-vseh-anagramm-v-stroke-Reshenie-zadachi-08-18)
