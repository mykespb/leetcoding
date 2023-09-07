#!/usr/bin/env python
# Mikhail Kolodin
# lc-mindiff.py 2023-09-07 2023-09-07 1.0

import itertools

null = None

def solve(root: list[int]) -> int:
    """solve 1 task"""

    arr = [x for x in root if x is not None]
    return min([
        abs(x[0] - x[1])
        for x in 
            itertools.combinations(arr, 2)
        ]
        )


def test(root: list[int]) -> None:
    """run 1 test"""

    print(f"{root=} => {solve(root)}")    


test(root = [4,2,6,1,3])
test(root = [1,0,48,null,null,12,49])

# root=[4, 2, 6, 1, 3] => 1
# root=[1, 0, 48, None, None, 12, 49] => 1


# Минимальная разница между узлами бинарного дерева

#  (https://leetcode.com/problems/minimum-distance-between-bst-nodes/)Сложность: Лёгкая

# Условие задачи: дается корень бинарного дерева поиска , верните минимальную разницу между значениями любых двух различных вершин в дереве.

# Пример:

# Ввод: root = [4,2,6,1,3]
# Вывод: 1

# Ввод: root = [1,0,48,null,null,12,49]
# Вывод: 1