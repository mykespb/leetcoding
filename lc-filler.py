#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2023
# 2023-03-18 2023-03-18 1.1 OK

from pprint import pp

def filler(arr, sr, sc, col):
    """fill all points"""

    global rows, cols, old, color
    rows = len(arr)
    cols = len(arr[0])
    color = col
    
    assert sr >= 0 and sr < rows and sc >= 0 and sc < cols and color > 0

    old = arr[sr][sc]
    put(arr, sr, sc)
    
def put(arr, sr, sc):
    """put 1 point and call others"""

    arr[sr][sc] = color

    if sr > 0 and arr[sr-1][sc] == old:
        put(arr, sr-1, sc)
    if sr < rows-1 and arr[sr+1][sc] == old:
        put(arr, sr+1, sc)
    if sc > 0 and arr[sr][sc-1] == old:
        put(arr, sr, sc-1)
    if sc < cols-1 and arr[sr][sc+1] == old:
        put(arr, sr, sc+1)

def test(arr, sr, sc, color):
    """print ins and outs tested"""

    pp(arr, width=20)
    print(f"{sr=}, {sc=}, {color=}")
    filler(arr, sr, sc, color)
    pp(arr, width=20)

test([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)

# Заливка

#  (https://leetcode.com/problems/flood-fill/)Сложность: Лёгкая 

# Условие задачи: дается изображение, которое представлено двумерной матрицей, где каждая ячейка означает значение пикселя.

# Также даются три числа sr, sc, color. Надо осуществить заливку, начиная с image[sr][sc].

# Заливка осуществляется в четырех направлениях от текущей ячейки, при этом изменяются только ячейки, которые имеют идентичное значение пикселя с базовой ячейкой.

# Пример:

# Ввод:  image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Вывод:  [[2,2,2],[2,2,0],[2,0,1]]
