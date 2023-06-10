#!/usr/bin/env python

# Mikhail Kolodin
# lc-izomorf.py 2023-06-10 2023-06-10 1.0

def solve(s: str, t: str) -> bool:
    """are string isomorphic?"""

    ls = len(s)
    lt = len(t)
    if ls != lt:
        return False
    
    pari = {}
    for i in range(ls):
        c = s[i]
        if c in pari:
            if pari[c] != t[i]:
                return False
        else:
            pari[c] = t[i]

    return True


def test(s: str, t: str):
    """print test results"""
    print(f"task: {s=}, {t=}, result: {solve(s, t)}")

test('egg', 'add')
test('foo', 'bar')

# task: s='egg', t='add', result: True
# task: s='foo', t='bar', result: False


# Изоморфизм строки (https://leetcode.com/problems/isomorphic-strings/)
#  (https://leetcode.com/problems/isomorphic-strings/)
# Сложность: Лёгкая

# Условие задачи: даны две строки s и t. Просят проверить их на изоморфность. 

# Две строки считаются изоморфными, если одной букве из одной строки ставится в соответствие уникальная буква из другой строки. Соответствие должно быть уникальным.

# Пример:

# Ввод: s = "egg", t = "add"
# Вывод: true

# Объяснение: "e" <--> "t", "g" <--> "d"

# Ввод: s = "foo", t = "bar"
# Вывод: false

# Объяснение: "f" <--> "b", "o" <--> "a", "o" <--> "r". Два символа из второй строки соответствуют одному символу из первой строки. 
