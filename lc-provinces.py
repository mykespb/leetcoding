#!/usr/bin/env python
# Mikhail Kolodin
# lc-provinces.py 2023-09-20 2023-09-20 1.0

from itertools import product

def solve(isConnected):
    """solve 1 task"""
    global size

    size = len(isConnected)

    pron = 0

    for rept in range(size):

        for i, j in product(range(size), range(size)):
            if isConnected[i][j]:
                pron += 1
                erase(isConnected, i)
                break
        else:
            break

    return pron


def erase(mat, i):
    """erase i-th node and its links"""
    global size

    todel = [j for j in mat[i] if j and j!=i]
    for k in range(size):
        mat[i][k] = 0
        mat[k][i] = 0

    for e in todel:
        erase(mat, e)


def test(isConnected):
    """run 1 test"""

    print(f"{isConnected=} => {solve(isConnected)}")    

test(isConnected = [[1,1,0],[1,1,0],[0,0,1]])

# isConnected=[[1, 1, 0], [1, 1, 0], [0, 0, 1]] => 2


# Количество провинций

#  (https://leetcode.com/problems/number-of-provinces/description/)
# Сложность: Средняя

# Условие задачи: даётся n провинций, какие-то из них соединены между собой, какие-то нет, также соблюдается правило транзитивности: если провинция «1» соединена с провинцией «2», а «2» соединена с «3» провинцией, то и «1» соединена с «3». 

# Провинцией является совокупность городов, объединённых между собой, но при этом отделенные от других, принадлежащих другим провинциям. 

# На вход даётся квадратичная матрица, в которой isConnected[i][j] = 1 - соединение между i - ым и j - - ым населенными пунктами (1 - имеется соединение, 0 - отсутствует). 

# Необходимо вычислить количество провинций. 

# Пример:

# Ввод: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Вывод: 2
# Объяснение: *во вложении
