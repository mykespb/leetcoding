#!/usr/bin/env python
# Mikhail Kolodin
# lc-minbridge.py 2023-09-19 2023-09-19 1.0

from itertools import product

SUPER = 9
TOBE = -2
WAVE = -3

def solve(grid):
    """solve 1 task"""
    global rows, cols

    rows = len(grid)
    cols = len(grid[0])

    # find 1st island
    # mark it as -1

    for i, j in product(range(rows), range(cols)):
        if grid[i][j] == 1:
            mark(grid, i, j, -1)
            break

    # find 2nd island
    # mark it as 1

    for i, j in product(range(rows), range(cols)):
        if grid[i][j] == 1:
            mark(grid, i, j, SUPER)
            break

    # start from 1 to infty:
    # make border around 1st island 
    # until it touches 2nd island

    for rept in range(max(rows, cols)):

        for pi, pj in product(range(rows), range(cols)):
            if grid[pi][pj] == 0:

                for ni, nj in (pi-1, pj), (pi+1, pj), (pi, pj-1), (pi, pj+1):
                    if ongrid(ni, nj) and grid[ni][nj] < 0 and grid[ni][nj] != TOBE:
                        grid[pi][pj] = TOBE

        for pi, pj in product(range(rows), range(cols)):
            if grid[pi][pj] == TOBE:

                for ni, nj in (pi-1, pj), (pi+1, pj), (pi, pj-1), (pi, pj+1):
                    if ongrid(ni, nj) and grid[ni][nj] == SUPER:
                        return rept+1

        for pi, pj in product(range(rows), range(cols)):
            if grid[pi][pj] == TOBE:
                grid[pi][pj] = WAVE

    # as soon as it touches, solution is found
    # ... or not found, alas (it cannot happen! error!)
    return 0


def mark(grid, i, j, color):
    """mark island"""
    
    # print(f"island {color} found at {i=}, {j=}")
    todo = []
    for point in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
        if ongrid(point[0], point[1]) and grid[point[0]][point[1]] == 1:
            todo.append(point)
    done = []
    grid[i][j] = color

    while todo:
        paint(grid, todo, done, color)


def paint(grid, todo, done, color):
    """recursively paint island"""

    if not todo:
        return
    
    for point in todo:
        if point in done: 
            continue
        i, j = point
        grid[i][j] = color
        done.append(point)

        for point in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
            if ongrid(point[0], point[1]) and grid[point[0]][point[1]] == 1:
                todo.append(point)


def ongrid(row, col):
    """check if point is on grid"""
    global rows, cols

    return (
        row >= 0 and row < rows and
        col >= 0 and col < cols
    )


def test(grid):
    """run 1 test"""

    print(f"{grid=} => {solve(grid)}")    


test(grid = [[0,1],[1,0]])
test(grid = [[0,1,0],[0,0,0],[0,0,1]])
test(grid = [[0,0,0],[1,0,0],[0,0,1]])
test(grid = [[1,0,0],[0,0,0],[0,0,1]])

# grid=[[0, 1], [1, 0]] => 1
# grid=[[0, 1, 0], [0, 0, 0], [0, 0, 1]] => 2
# grid=[[0, 0, 0], [1, 0, 0], [0, 0, 1]] => 2
# grid=[[1, 0, 0], [0, 0, 0], [0, 0, 1]] => 3


# Мост наименьшей длины (https://leetcode.com/problems/shortest-bridge/)

# Сложность: Средняя

# Условие задачи: на вход подается матрица, в которой 1 - суша, 0 - вода.

# Остров представляет из себя совокупность частей суши, соединенных в четырех направлениях. На решетке существуют только два острова.

# Можно изменить 0 на 1 для соединения двух островов в один. 

# Необходимо посчитать количество смен нулей на единицу для соединения двух островов.

# Пример:

# Ввод: grid = [[0,1],[1,0]]
# Вывод: 1
# Объяснение:

# Ввод:  grid = [[0,1,0],[0,0,0],[0,0,1]]
# Вывод: 2
