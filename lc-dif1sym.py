#!/usr/bin/env python

# Mikhail Kolodin
# lc-dif1sym.py 2023-07-05 2023-07-05 1.0

def diff(s1:str, s2:str) -> bool:
    """do strings differ exactly by 1 char"""

    dif = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            dif += 1
            if dif>1:
                return False
    return dif == 1

def solve(d: list[str]) -> bool:
    """solve it"""
    
    for i1 in range(len(d) - 1):
        for i2 in range(i1, len(d)):
            if diff(d[i1], d[i2]) == 1:
                # print(d[i1], d[i2])
                return True
            
    return False

def test(d: list[str]) -> None:
    print(f"{d=} => {solve(d)}")

test(["abcd", "acbd", "aacd"])
test(["ab", "cd", "yz"])

## abcd aacd
# d=['abcd', 'acbd', 'aacd'] => True
# d=['ab', 'cd', 'yz'] => False

# Строки отличающиеся на один символ

#  (https://leetcode.com/problems/strings-differ-by-one-character/)Сложность задачи: Средняя

# Условие задачи:
# Дан список строк dict, где все строки имеют одинаковую длину.

# Верните true, если в одном и том же индексе есть 2 строки, которые отличаются только на 1 символ, в противном случае возвращает false.

# Пример:
# Ввод: dict = ["abcd","acbd", "aacd"]
# Вывод: true
# Объяснение: Строки "abcd" и "aacd" отличаются только одним символом в индексе 1.

# Ввод: dict = ["ab","cd","yz"]
# Вывод: false
