#!/usr/bin/env python
# Mikhail Kolodin
# lc-bintreeright.py 2023-10-08 2023-10-08 1.0

import math

null = None

def solve(root: list[int]) -> int:
    """solve 1 task"""

    out = [root[0]]
    size = 1

    for line in range(1, len(root)):
        plus = 2 ** line
        size += plus
        if size > len(root):
            break
        out.append(root[size - 1])

    return out

def test(root: list[int]) -> None:
    """run 1 test"""

    print(f"{root=} => {solve(root)}")    


test(root = [1,2,3,null,5,null,4])
test(root = [1,null,3])

# root=[1, 2, 3, None, 5, None, 4] => [1, 3, 4]
# root=[1, None, 3] => [1, 3]

# print(
#     [2**p - 1 for p in range(1, 10) ]
# )

# Бинарное дерево с правой стороны (https://leetcode.com/problems/binary-tree-right-side-view/)

# Сложность:  Средняя 

# Условие задачи: на вход подается бинарное дерево, представим, что стоим справа, необходимо вывезти значения, которые будут видны с этой стороны.

# Пример:

# Ввод: root = [1,2,3,null,5,null,4]
# Вывод: [1,3,4]
# Объяснение: * во вложении

# Ввод: root = [1,null,3]
# Вывод: [1, 3]