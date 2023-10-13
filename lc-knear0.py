#!/usr/bin/env python
# Mikhail Kolodin
# lc-knear0.py 2023-10-13 2023-10-13 1.0

import math

def solve(points, k):
    """solve 1 task"""

    return sorted(points, key = lambda p: euclide(p))[:k]


def euclide(p):
    """calc euclide distance"""

    return math.sqrt(p[0]**2 + p[1]**2)


def test(points, k):
    """run 1 test"""

    print(f"\n{points=}, {k=} => {solve(points, k)}")    

test(points = [[1,3],[-2,2]], k = 1)
test(points = [[1,3],[-2,2]], k = 2)


# points=[[1, 3], [-2, 2]], k=1 => [[-2, 2]]
# points=[[1, 3], [-2, 2]], k=2 => [[-2, 2], [1, 3]]

# K - ближайших точек к началу координат (https://leetcode.com/problems/k-closest-points-to-origin/)

# Сложность:  Средняя 

# Условие задачи: дан массив точек на плоскости, характеризующихся соответствующими декартовыми координатами. Также дается число k, которое обозначает количество точек, наиболее близких к началу координат, которые надо вывести. Расстояние измеряется через расстояние Евклида.

# Гарантируется уникальность ответа.

# Пример:

# Ввод:  points = [[1,3],[-2,2]], k = 1
# Вывод:  [[-2,2]]
