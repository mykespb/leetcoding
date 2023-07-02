#!/usr/bin/env python

# Mikhail Kolodin
# lc-islands.py 2023-07-02 2023-07-02 1.0

from pprint import pp

def solve():
    """solve it"""
    global grid, erasor, erased

    erasor = []
    erased = []
    count = 0

    need = True
    while need:
        need = False

        found, i, j = findisle()
        if found:
            count += 1
            need = True
            erasor = [(i, j)]
            # print("island at", i, j)
            eraseisle()

    return count

def findisle():
    """find island"""
    global grid

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                return True, i, j
            
    return False, 0, 0

def eraseisle():
    """erase island from grid"""
    global grid, erasor, erased

    while erasor:

        i, j = erasor.pop()

        grid[i][j] = '0'
        erased += [(i, j)]

        for ip, jp in [[-1, 0], [1, 0], [0, -1], [0, 1]]:

            ix = i + ip
            jx = j + jp

            if ix >= 0 and ix < len(grid) and jx >= 0 and jx < len(grid[0]) and grid[ix][jx] == "1" and (ix, jx) not in erased:
                erasor += [(ix, jx)]

def test() -> None:
    """print test results"""
    global grid

    print("\n------------------------------------\n")
    pp(grid)
    print(solve())

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

test()

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

test()


# ------------------------------------

# [['1', '1', '1', '1', '0'],
#  ['1', '1', '0', '1', '0'],
#  ['1', '1', '0', '0', '0'],
#  ['0', '0', '0', '0', '0']]
# 1

# ------------------------------------

# [['1', '1', '0', '0', '0'],
#  ['1', '1', '0', '0', '0'],
#  ['0', '0', '1', '0', '0'],
#  ['0', '0', '0', '1', '1']]
# 3


# NB: условие задачи и пример противоречат друг другу,
# по-разному определено понятие соседа.
# Решаем для случая, который указан в 2 примерах, 
# без диагоналей,
# а не того, который на картинке.

# Определение количества островов
#  (https://leetcode.com/problems/number-of-islands/)
# Сложность: Средняя

# Условие задачи: дан двумерный массив размера m x n. "1" отвечает за сушу, "0" - за океан. Требуется опеределить количество островов, расположенных на карте. 

# Островом считается территория, образованная из "1", расположенных сверху, справа, снизу и слева относительно друг друга. 

# Пример: 

# Ввод: 
# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Вывод: 1

# Ввод: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Вывод: 3
