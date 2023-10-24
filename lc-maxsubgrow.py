#!/usr/bin/env python
# Mikhail Kolodin
# lc-maxsubgrow.py 2023-10-24 2023-10-24 1.0

from itertools import combinations 

def solve(nums: list[int]) -> int:
    """solve 1 task"""

    for lena in range(len(nums), 0, -1):

        nseq = 0

        for seq in combinations(nums, lena):

            if good(seq):
                nseq += 1

        if nseq:
            break

    return nseq


def good(seq):
    """check if sequenece is good (growing)"""

    for i in range(len(seq) - 1):
        if seq[i] >= seq[i+1]:
            return False
        
    return True


def test(nums: list[int]) -> None:
    """run 1 test"""

    print(f"\n{nums=} => {solve(nums)}")

test(nums = [1,3,5,4,7])
test(nums = [2,2,2,2,2])


# nums=[1, 3, 5, 4, 7] => 2

# nums=[2, 2, 2, 2, 2] => 5

# Количество возрастающих подпоследовательностей наибольшей длины  (https://leetcode.com/problems/number-of-longest-increasing-subsequence/)

# Сложность: Средняя

# Условие задачи: дан массив целых чисел, надо посчитать количество возрастающих подпоследовательностей наибольшей длины. Подпоследовательность (ее элементы) должна строго возрастать.

# Пример:

# Ввод: nums = [1,3,5,4,7]
# Вывод: 2
# Объяснение: есть две возрастающие подпоследовательности одинаковой длины: [1, 3, 4, 7] и [1, 3, 5, 7]

# Ввод: nums = [2,2,2,2,2]
# Вывод: 5
# Объяснение: в данном массиве есть 5 подпоследовательностей длины 1.

# Решение задачи (https://telegra.ph/Kolichestvo-vozrastayushchih-podposledovatelnostej-naibolshej-dliny-Reshenie-zadachi-10-04)