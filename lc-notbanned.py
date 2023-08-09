#!/usr/bin/env python
# Mikhail Kolodin
# lc-notbanned.py 2023-08-09 2023-09-09 1.0

from string import ascii_letters as letters
from collections import Counter

def solve(paragraph: str, banned: list[str]):
    """solve complete task"""
    
    para = "".join(x for x in paragraph if x in letters + " ")
    paras = para.lower().split()
    paras = list(filter(lambda x: x not in banned, paras))
    cnt = Counter(paras)
    return cnt.most_common()[0][0]


def test(paragraph: str, banned: list[str]):
    """run 1 test"""
    print(f"task: {paragraph=}, {banned=} => {solve(paragraph, banned)}")

test(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"])
test(paragraph = "a.", banned = [])

# task: paragraph='Bob hit a ball, the hit BALL flew far after it was hit.', banned=['hit'] => ball
# task: paragraph='a.', banned=[] => a

# Наиболее частое слово

#  (https://leetcode.com/problems/most-common-word/)
# 
# Сложность: Лёгкая

# Условие задачи: дается строковый абзац и строковый массив запрещенных слов banned возвращают наиболее часто встречающееся слово, которое не запрещено. Гарантируется, что есть хотя бы одно слово, которое не запрещено, и что ответ уникален.

# Слова в абзаце не учитывают регистр, и ответ должен быть возвращен в нижнем регистре.

# Пример:

# Ввод: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Вывод: "ball"

# Ввод: paragraph = "a.", banned = []
# Вывод: "a"
