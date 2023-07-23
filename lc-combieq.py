#!/usr/bin/env python

# Mikhail Kolodin
# lc-combyeq.py 2023-07-13 2023-07-13 1.0

from itertools import combinations as func

def solve(n, k):

    seq = [i for i in range(1, n+1)]
    return list(func(seq, k))

def test(n, k):

    print(f"{n=}, {k=}, result={solve(n, k)}")

test(n=4, k=2)
test(n=1, k=1)

# n=4, k=2, result=[(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
# n=1, k=1, result=[(1,)]

# Комбинации

#  (https://leetcode.com/problems/combinations/)Сложность: Средняя

# Условие задачи: даны два целых положительных числа n и k. Надо вывести все комибинации, состоящие из k-чисел в диапазоне [1, n]. 

# Пример:

# Ввод: n = 4, k = 2
# Вывод:[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

# Объяснение: число перестановок равно 6. Важным моментом является неупорядоченность чисел внутри самих комбинаций, то есть пары [1,2] и [2,1] являются одинаковыми. 

# Ввод: n = 1, k = 1
# Вывод: [[1]]

# Коментарий: по-видимому, можно считать нормальным результат, в котором внутри кортежи, а не вложенные списки; задча-то надъязыковая.