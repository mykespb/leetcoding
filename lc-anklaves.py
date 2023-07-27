#!/usr/bin/env python
# Mikhail Kolodin
# lc-anklaves.py 2023-07-27 2023-07-27 1.0

def solve():
    global grid, rows, cols

    rows = len(grid)
    cols = len(grid[0])

    for i, j in (
        [(0, k) for k in range(cols) ] +
        [(rows-1, k) for k in range(cols) ] +
        [(k, 0) for k in range(1, rows-1) ] +
        [(k, cols-1) for k in range(1, rows-1) ]
    ):
        if grid[i][j]:
            rek(i, j)

    return sum([sum(row) for row in grid])


def rek(i, j):
    global grid, rows, cols

    if i<0 or i>=rows or j<0 or j>=cols:
        return
    if grid[i][j]:
        grid[i][j] = 0
        rek(i-1, j)
        rek(i+1, j)
        rek(i, j-1)
        rek(i, j+1)


def test():
    print(f"\n{grid=} => {solve()}")

grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
test()
grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
test()

# grid=[[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]] => 3

# grid=[[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]] => 0

# Количество анклавов

#  (https://leetcode.com/problems/number-of-enclaves/)Сложность: Средняя

# Условие задачи: дана двумерная решетка, где 0 - море, 1 - суша. 

# Движения могут осуществляться в одном из четрыех направлений: вверх, вниз, вправо, влево. 

# Необходимо посчитать количество анклавов. Анклавом является участок суши, который не прилегает ни к одной из границ заданной площадки. 

# Пример:

# Ввод:  grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# Вывод: 3
# Объяснение: на данном поле есть три участка суши, отделенных от границ водой, и один элемент, прилегающий к границе. 

# Ввод: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# Вывод: 0
