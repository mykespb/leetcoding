#!/usr/bin/env python

# Mikhail Kolodin
# lc-toplic.py 2023-07-19 2023-07-19 1.0

def solve(matrix: list[list[int]]) -> bool:
    """solve problem"""

    rows = len(matrix)
    cols = len(matrix[0])

    times = cols + rows - 1

    for rept in range(-rows+1, cols):

        val = None
        for row in range(rows):
            col = rept + row

            if col < 0 or col >= cols:
                continue

            if val is not None:
                if val != matrix[row][col]:
                    return False

            else:
                val = matrix[row][col]

    return True

def test(matrix: list[list[int]]) -> None:
    """run 1 test"""

    print(matrix, solve(matrix))

test([[1,2,3,4],[5,1,2,3],[9,5,1,2]])
# [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]] True

# Матрица Топлица

#  (https://leetcode.com/problems/toeplitz-matrix/)
# Сложность: Лёгкая Средняя Тяжёлая

# Условие задачи: дается матрица mxn, верните значение true, если матрица является Теплициевой. В противном случае верните значение false.

# Матрица является Теплициевой, если каждая диагональ от верхнего левого края до нижнего правого имеет одинаковые элементы.

# Пример:

# Ввод: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# Вывод: true
