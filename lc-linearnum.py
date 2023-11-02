#!/usr/bin/env python
# Mikhail Kolodin
# lc-linearnum.py 2023-09-01 2023-09-01 1.1

from itertools import combinations

EPS = 1e-5

def solve(points: list[list[int]]) -> int:
    """solve 1 task"""

    plen = len(points)
    if plen < 3:
        return plens
    
    points.sort()

    for clen in range(plen, 3, -1):

        for comb in combinations(points, clen):
            if linear(comb):
                return clen

    return 3


def linear(arr: tuple[list[int]]) -> bool:
    dx = arr[1][0] - arr[0][0]
    dy = arr[1][1] - arr[0][1]
    drecl = dy / dx if dx else 0

    for p in arr[2:]:
        cx = p[0] - arr[0][0]
        cy = p[1] - arr[0][1]
        crecl = cy / cx if cx else 0

        if drecl == crecl == 0:
            return p[0] == arr[0][0]

        if abs(drecl - crecl) > EPS:
            return False
        
    return True


def test(points: list[list[int]]) -> None:
    """run 1 test"""

    print(f"{points=} => {solve(points)}")    

test(points = [[1,1],[2,2],[3,3]])
test(points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]])

# points=[[1, 1], [2, 2], [3, 3]] => 3
# points=[[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]] => 4

# Количество точек на прямой

#  (https://leetcode.com/problems/max-points-on-a-line/)
# Сложность: Тяжёлая

# Условие задачи: дается массив точек, где точки [i] = [xi, yi] представляют точку на плоскости X-Y, верните максимальное количество точек, которые лежат на одной прямой.

# Пример:

# Ввод: points = [[1,1],[2,2],[3,3]]
# Вывод: 3

# Ввод: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Вывод: 4