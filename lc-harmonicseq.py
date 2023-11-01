#!/usr/bin/env python
# Mikhail Kolodin
# lc-harmonicseq.py 2023-08-04 2023-09-04 1.0

import itertools

def solve(nums):
    """solve complete task"""

    nlen = len(nums)
    longest = 0

    for n in range(2**nlen):
        pattern = [int(x) for x in list(f"{n:0{nlen}b}")]
        selected = list(itertools.compress(nums, pattern))

        if not selected:
            continue
        if max(selected) - min(selected) == 1:
            longest = max(longest, len(selected))

    return longest


def test(nums):
    """run 1 test"""
    print(f"task: {nums=} => {solve(nums)}")

test([1, 3, 2, 2, 5, 2, 3, 7])
test([1, 2, 3, 4])
test([])

# task: nums=[1, 3, 2, 2, 5, 2, 3, 7] => 5
# task: nums=[1, 2, 3, 4] => 2
# task: nums=[] => 0

# Гармоничная подпоследовательность наибольшей длины

#  (https://leetcode.com/problems/longest-harmonious-subsequence/)
# Сложность: Средняя 

# Условие задачи: Мы определяем гармоничный массив как массив, в котором разница между его максимальным значением и минимальным значением равна ровно 1.

# Дается целочисленный массив nums, верните длину его самой длинной гармоничной подпоследовательности среди всех его возможных подпоследовательностей.

# Подпоследовательность массива - это последовательность, которая может быть получена из массива путем удаления некоторых элементов или вообще без них без изменения порядка остальных элементов.

# Пример:

# Ввод: nums = [1,3,2,2,5,2,3,7]
# Вывод: 5
# Объяснение: [3,2,2,2,3] - гармоничная подпоследовательность наибольшей длины.

# Ввод: nums = [1,2,3,4]
# Вывод: 2