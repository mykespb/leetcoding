#!/usr/bin/env python

# Mikhail Kolodin
# lc-unicocc.py 2023-06-09 2023-06-09 1.0

from collections import Counter

def solve(arr: list[int]) -> bool:
    """make palins"""

    c = Counter(arr)
    cc = Counter(c.values())
    return all(map(lambda x: x == 1, cc.values()))
    

def test(s: list[int]):
    """print test results"""
    print(f"\ntask:   {s=}\nresult: {solve(s)}")

test([1, 2, 2, 1, 1, 3])

# task:   s=[1, 2, 2, 1, 1, 3]
# result: True


# Уникальное количество вхождений

# Условие задачи:
# Дан массив целых чисел arr, верните true, если количество вхождений каждого значения в массиве уникально, или false в противном случае.

# Пример:
# Ввод: arr = [1,2,2,1,1,3]
# Вывод: true
# Объяснение: Значение 1 имеет 3 вхождения, 2 имеет 2, а 3 имеет 1. Никакие два значения не имеют одинакового количества вхождений.

# Ввод: arr = [1,2]
# Вывод: false

# Решение задачи (https://telegra.ph/Reshenie-zadachi-07-21-2)
