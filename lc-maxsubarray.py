#!/usr/bin/env python

# Mikhail Kolodin
# lc-maxsubarray.py 2023-06-08 2023-06-08 1.0


def maxsub(arr: list[int]) -> int:
    """find max subarray"""

    msum = None

    for start in range(len(arr)):
        for slen in range(1, len(arr) - start + 1):
            asum = sum(arr[start: start+slen])
            if msum is None or asum > msum:
                msum = asum

    return msum


def test(nums):
    """ show """
    print(f"{nums=} -> {maxsub(nums)}")


test([-2, 1, -3, 4, -1, 2, 1, -5, 4])
test([5, 4, -1, 7, 8])

# nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4] -> 6
# nums=[5, 4, -1, 7, 8] -> 23

# Максимальный подмассив (https://leetcode.com/problems/maximum-subarray/)

# Сложность: Средняя

# Условие задачи: дан целочисленный массив, необходимо найти в нем такой подмассив, сумма элементов в котором будет максимальной. 

# Подмассивом называется последовательная часть исходного массива. 

# Пример:

# Ввод: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Вывод: 6

# Объяснение: 4,-1,2,1] имеет наибольшую сумму 6.

# Ввод: nums = [5,4,-1,7,8]
# Вывод: 23

# Решение задачи (https://telegra.ph/Maksimalnyj-podmassiv-Reshenie-zadachi-08-28)
