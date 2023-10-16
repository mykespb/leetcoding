#!/usr/bin/env python
# Mikhail Kolodin
# lc-subnondup.py 2023-10-16 2023-10-16 1.0

from itertools import combinations as func

def solve(nums):
    """solve 1 task"""

    nums = sorted(set(nums))
    out = []

    for lena in range( len(nums) + 1 ):
        plus = sorted( func(nums, lena) )
        out += [ list(x) for x in plus ]

    return out


def test(nums):
    """run 1 test"""

    print(f"\n{nums=} => {solve(nums)}")    

test(nums = [1, 2, 3])
test(nums = [1, 2, 3, 3, 3, 2])
test(nums = [0])
print()

# nums=[1, 2, 3] => [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]

# nums=[1, 2, 3, 3, 3, 2] => [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]

# nums=[0] => [[], [0]]

# Подмножества (https://leetcode.com/problems/subsets/)

# Сложность: Средняя

# Условие задачи: дан массив из целых чисел, необходимо вывести все подмножества исходного массива, которые не содержат дубликаты.

# Пример:

# Ввод: nums = [1,2,3]
# Вывод: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Ввод: nums = [0]
# Вывод: [[],[0]]