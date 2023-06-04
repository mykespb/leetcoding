#!/usr/bin/env python

# Mikhail Kolodin
# lc-rotmatplace.py 2023-06-05 2023-06-05 1.0

def rotator(mat):
    """ rotate """
    
    size = len(mat)
    for level in range(size // 2):
        for off in range(size - 2 * level - 1):
            t = mat[level][level + off]
            mat[level][level + off] = mat[size - level - off - 1][level]
            mat[size - level - off - 1][level] = mat[size - level - 1][size - level - off - 1]
            mat[size - level - 1][size - level - off - 1] = mat[level + off][size - level - 1]
            mat[level + off][size - level - 1] = t

    return mat


def test(mat):
    """ show """
    print("source matrix: ", mat)
    rom = rotator(mat)
    print("rotated matrix:", rom)

test([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
test([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])

# source matrix:  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# rotated matrix: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
# source matrix:  [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
# rotated matrix: [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]

# Вращение изображения

#  (https://leetcode.com/problems/rotate-image/)Сложность: Средняя

# Условие задачи: дан двумерный массив, представляющий из себя изоражение, необходимо провращать данное изображение на 90 градусов по часов. 

# Решение должно фактически изменять исходный массив, не создавая новой матрицы. 

# Пример:

# Ввод: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Вывод:  [[7,4,1],[8,5,2],[9,6,3]]

# Ввод: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Вывод: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
