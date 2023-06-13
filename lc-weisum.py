#!/usr/bin/env python

# Mikhail Kolodin
# lc-weisum.py 2023-06-13 2023-06-13 1.1

def solve(nr):
    """give weighted sum of list"""
    global maxdepth, adds

    prep(nr, 1)

    summa = 0
    for n, l in adds:
        summa += n * (maxdepth - l + 1)

    return summa


def prep(l, level):
    """cal part"""
    global maxdepth, adds

    maxdepth = max(maxdepth, level)

    for e in l:
        if type(e) == int:
            adds += [[e, level]]
        else:
            prep(e, level+1)


def test(nestedList):
    """print test results"""
    global maxdepth, adds

    maxdepth = 0
    adds = []
    
#    print(f"task: {nestedList=},\nresult: {maxdepth=}, {adds=}, {solve(nestedList)}")
    print(f"task: {nestedList=},\nresult: {solve(nestedList)}")

test([[1, 1], 2, [1, 1]])
test([1, [4, [6]]])

# Весовая сумма списка 2

#  (https://leetcode.com/problems/nested-list-weight-sum-ii/)Сложность задачи: Средняя

# Условие задачи:
# Вам дан вложенный список целых чисел nestedList. Каждый элемент является либо целым числом, либо списком, элементы которого также могут быть целыми числами или другими списками.

# Глубина целого числа — это количество списков, внутри которых оно находится. Например, во вложенном списке [1,[2,2],[[3],2],1] каждому целочисленному значению соответствует его глубина. Пусть maxDepth будет максимальной глубиной любого целого числа. Вес целого числа равен maxDepth - (глубина целого числа) + 1.

# Верните сумму каждого целого числа во вложенном списке, умноженную на его вес.

# Значения целых чисел во вложенном списке находятся в диапазоне [-100, 100].
# Максимальная глубина любого целого числа меньше или равна 50.

# Пример:
# Ввод: nestedList = [[1,1],2,[1,1]]
# Вывод: 8
# Объяснение: Четыре единицы с весом 1, одна двойка с весом 2.
# 1*1 + 1*1 + 2*2 + 1*1 + 1*1 = 8

# Ввод: nestedList = [1,[4,[6]]]
# Вывод: 17
