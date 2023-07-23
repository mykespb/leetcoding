#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2023-07-24 2023-07-24 1.1

def go (tri, level, pos):
    if level >= len(tri):
        return 0
    return tri[level][pos] + min(go(tri, level+1, pos), go(tri, level+1, pos+1))


def test(tri):
    print(f"{tri=} => {go(tri, 0, 0)}")


test([[2],[3,4],[6,5,7],[4,1,8,3]])
test([[1], [0, 0]])
test([[1]])

# tri=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]] => 11
# tri=[[1], [0, 0]] => 1
# tri=[[1]] => 1

# Треугольник (https://leetcode.com/problems/triangle/)

# Сложность: Средняя

# Условие задачи: дан двумерный массив, надо посчитать минимальную сумму от вершины тругольника до его основания. 
# На каждом шаге, анходясь на i-ой позиции можно перемещаться на i-ую или i+1 позицию следующего ряда. 

# Пример:
# Ввод: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Вывод: 11

# Объяснение: треуголльник выглядит следующим образом:

#    2
#   3 4
#  6 5 7
# 4 1 8 3

# Минимальный путь выглядит следующим образом: 2 + 3 + 5 + 1 = 11.
