#!/usr/bin/env python
# Mikhail Kolodin
# lc-pathminsum.py 2023-09-21 2023-09-21 1.0

from itertools import product

def solve(grid):
    """solve 1 task"""
    global rows, cols, lastcol, lastrow, minsum

    rows = len(grid)
    cols = len(grid[0])
    lastrow = rows - 1
    lastcol = cols -1

    minsum = 999999
    cursum = 0

    go(grid, 0, 0, cursum)

    return minsum


def go(grid, i, j, cursum):
    """make recursive search"""
    global rows, cols, lastcol, lastrow, minsum

    cursum += grid[i][j]

    if cursum > minsum:
        return
    
    if i == lastrow and j == lastcol:
        minsum = min(minsum, cursum)
        return
    
    if i < lastrow:
        go(grid, i+1, j, cursum)

    if j < lastcol:
        go(grid, i, j+1, cursum)
    

def test(grid):
    """run 1 test"""

    print(f"{grid=} => {solve(grid)}")    


test(grid = [[1,3,1],[1,5,1],[4,2,1]])

# grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]] => 7


# Путь минимальной суммы

#  (https://leetcode.com/problems/minimum-path-sum/)Сложность: Средняя 

# Условие задачи: дается двумерная матрица, заполненная неотрицательными числами. Необходимо найти путь из левого верхнего угла в правый нижний, который имеет наименьшую сумму. 

# Двигаться можно лишь вправо и вниз. 

# Пример:

# Ввод: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Вывод: 7
# Объяснение: *во вложении