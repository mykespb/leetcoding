#!/usr/bin/env python

# Mikhail Kolodin
# lc-minaloop.py 2023-12-11 2023-12-11 1.0


def solve(n, edges):
    """solve problem"""

    nfrom = [x[0] for x in edges]
    nto   = [x[1] for x in edges]

    good = sorted( set(nfrom) - set(nto) )

    return good


def test(n, edges):
    """run 1 test"""

    print(f"{n=}, {edges=} => {solve(n, edges)}")

test(n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]])

# n=6, edges=[[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]] => [0, 3]


# Минимальное количество ребер

#  (https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/description/)
# Сложность: Средняя 

# Условие задачи: дается ациклический направленный граф с вершинами, пронумерованными от 0 до n-1.

# Необходимо найти наименьшее количество ребер в графе такое что, можно было бы обойти все узлы.

# Пример:

# Ввод: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
# Вывод: [0,3]

# NB: условие некорректное!
