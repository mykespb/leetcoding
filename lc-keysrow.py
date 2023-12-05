#!/usr/bin/env python

# Mikhail Kolodin
# lc-keysrow.py 2023-12-05 2023-12-05 1.0

# keyboards by rows
kbd = ("`1234567890-=~!@#$%^&*()_+", "qwertyuiop[]\\", "asdfghjkl;'\"", "zxcvbnm,./", " ")

# key to row
c2r = {}
for i, row in enumerate(kbd):
    for c in row:
        c2r[c] = i
    
# print(c2r)

def solve(words: list[str]) -> list[str]:
    """process 1 word"""

    out = []

    for word in words:

        if len(word) < 2:
            return out.append(word)
        
        sword = word.lower()

        ptn = c2r[sword[0]]

        for c in sword[1:]:
            if c2r[c] != ptn:
                break
        else:
            out.append(word)

    return out


def test(words: list[str]):
    """print test results"""

    print(f"{words=} => {solve(words)}")


test(["Hello","Alaska","Dad","Peace"])
test(["omk"])

# words=['Hello', 'Alaska', 'Dad', 'Peace'] => ['Alaska', 'Dad']
# words=['omk'] => []


# Ряд клавиатуры
#  (https://leetcode.com/problems/keyboard-row/)
# Сложность: Лёгкая 

# Условие задачи: дается массив из строк, необходимо вернуть те строки из массива, которые могут быть набраны лишь при использовании знаков из одного ряда. 

# Пример:

# Ввод: words = ["Hello","Alaska","Dad","Peace"]
# Вывод:  ["Alaska","Dad"]
# Объяснение:

# Ввод: words = ["omk"]
# Вывод: [ ]
