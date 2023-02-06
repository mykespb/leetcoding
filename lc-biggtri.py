#!/usr/bin/env python
# Mikhail Kolodin, 2023
# 2023-02-06 2023-02-06 1.0

from itertools import combinations
from math import sqrt

def findtri(xy):

    # to store best result
    best = {'asq': -1, 'atri': None}

    # try all possible triangles
    for num, tri in enumerate(combinations(xy, 3)):
        # ~ print(num, tri)

        a, b, c = sides(tri)
        # ~ print(f"{a=}, {b=}, {c=}")
    
        if is_tri(a, b, c):
            if (sq := square(a, b, c)) > best['asq']:
                best = {'asq': sq, 'atri': tri}

    if best['atri']:
        print(f"\n{best=}\n")


def sides(tri):
    a = dist(tri[0], tri[1])
    b = dist(tri[0], tri[2])
    c = dist(tri[1], tri[2])
    return a, b, c


def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    d = sqrt(dx*dx + dy*dy)
    return d
    

def square(a, b, c):
    p = (a + b + c) / 2.
    # ~ print(f"{p=}")
    s = sqrt( p * (p-a) * (p-b) * (p-c) )
    # ~ print(f"square={s}")
    return s
   

def is_tri(a, b, c):
    return (a < b+c) and (b < a+c) and (c < a+b)


# tests

findtri( [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]] )
findtri( [[1, 0], [0, 0], [0, 1]] )


# ~ Треугольник наибольшей площади

 # ~ (https://leetcode.com/problems/largest-triangle-area/)Сложность: Лёгкая 

# ~ Условие задачи: дается массив точек на плоскости X-Y, где точки [i] = [xi, yi], верните площадь самого большого треугольника, который может быть образован любыми тремя различными точками. Будут приняты ответы в пределах 10-5 от фактического ответа.

# ~ Пример:

# ~ Ввод:  points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# ~ Вывод: 2.00000
# ~ Объяснение:

# ~ Ввод: points = [[1,0],[0,0],[0,1]]
# ~ Вывод:  0.50000

# ~ Решение задачи (https://telegra.ph/Treugolnik-naibolshej-ploshchadi-Reshenie-zadachi-02-04)


# ~ best={'asq': 1.9999999999999993, 'atri': ([0, 0], [0, 2], [2, 0])}


# ~ best={'asq': 0.49999999999999983, 'atri': ([1, 0], [0, 0], [0, 1])}
