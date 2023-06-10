#!/usr/bin/env python

# Mikhail Kolodin
# lc-grupana.py 2023-06-10 2023-06-10 1.0

def solve(strs: str) -> list[str]:
    """find groups of anagrams"""

    res = {}

    for s in strs:
        key = "".join(sorted(list(s)))
        if key in res:
            res[key] += [s]
        else:
            res[key] = [s]

    return [v for v in res.values()]


def test(strs: str) -> list[str]:
    """print test results"""
    print(f"task: {strs=}, result: {solve(strs)}")

test(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
test([''])

# task: strs=['eat', 'tea', 'tan', 'ate', 'nat', 'bat'], result: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
# task: strs=[''], result: [['']]

# Групповые анаграммы

#  (https://leetcode.com/problems/group-anagrams/)Сложность задачи: Средняя

# Условие задачи:
# Дан массив строк strs. Требуется сгруппировать анаграммы вместе. Вы можете вернуть ответ в любом порядке.

# Анаграмма — это слово или фраза, образованная путем перестановки букв другого слова или фразы, обычно с использованием всех исходных букв ровно один раз.

# Пример:
# Ввод: strs = ["eat","tea","tan","ate","nat","bat"]
# Вывод: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Ввод: strs = [""]
# Вывод: [[""]]
