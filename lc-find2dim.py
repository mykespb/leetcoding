#!/usr/bin/env python

# Mikhail Kolodin
# lc-find2dim.py 2023-07-22 2023-07-22 1.0

def solve(matrix, target) -> bool:
    """solve the problem"""

    rows = len(matrix)
    cols = len(matrix[0])

    i = 0
    j = cols -1

    while True:
        cur = matrix[i][j]

        if cur == target:
            return True
        
        if cur > target:
            j -= 1
            if j < 0:
                return False
            continue

        i += 1
        if i >= rows:
            return False


def test(matrix, target) -> bool:
    """run 1 test"""

    print(f"{matrix=}, {target=}, result={solve(matrix, target)}")

test(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5)
test(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20)

# matrix=[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], target=5, result=True
# matrix=[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], target=20, result=False

# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true

# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
# Output: false