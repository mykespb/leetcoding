#!/usr/bin/env python

# Mikhail Kolodin
# lc-tripascal.py 2023-06-10 2023-06-10 1.1

def solve(nr):
    """give triangle of pascal"""

    tri = [[1]]
    if nr < 2:
        return tri
    
    pred = [1]

    for row in range(1, nr):
        pred = [0] + pred + [0]
        succ = [pred[i] + pred[i+1] for i in range(len(pred) - 1)]
        pred = succ
        tri += [pred]

    return tri


def test(numRows):
    """print test results"""
    print(f"task: {numRows=},\nresult: {solve(numRows)}")

test(5)
test(1)
test(2)

# Треугольник Паскаля

#  (https://leetcode.com/problems/pascals-triangle/)Сложность задачи: Легкая

# Условие задачи:
# Дано целое число numRows, верните первые numRows треугольника Паскаля.

# В треугольнике Паскаля каждое число является суммой двух чисел непосредственно над ним, как показано на гифке выше.

# Пример:
# Ввод: numRows = 5
# Вывод: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Ввод: numRows = 1
# Вывод: [[1]]

# Решение задачи (https://telegra.ph/Reshenie-zadachi-07-27)