#!/usr/bin/env python

# Mikhail Kolodin
# lc-pivotel.py 2023-06-08 2023-06-08 1.0


def pivot(arr: list[int]) -> int:
    """find max subarray"""

    for ind in range(len(arr)):
        if sum(arr[:ind]) == sum(arr[ind+1:]):
            return ind
    return -1


def test(nums):
    """ show """
    print(f"{nums=} -> {pivot(nums)}")


test([1, 7, 3, 6, 5, 6])
test([1, 2, 3])
test([2, 1, -1])

# nums=[1, 7, 3, 6, 5, 6] -> 3
# nums=[1, 2, 3] -> -1
# nums=[2, 1, -1] -> 0

# Нахождение опорного элемента

#  (https://leetcode.com/problems/find-pivot-index/)Сложность: Лёгкая 

# Условие задачи: дан массив, состоящий из целых чисел. Необходимо вернуть опорный элемент массива. 

# Опорным называется такое число массива, относительно которого сумма элементов находящихся слева, равна сумме элементов, расположенных справа. 

# Необходимо вернуть индекс самого левого опороного элемента, в случае отсутствия такового - вернуть -1. 

# Пример:

# Ввод: nums = [1,7,3,6,5,6]
# Вывод: 3

# Объяснение: 
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11

# Ввод: nums = [1,2,3]
# Вывод: -1

# Ввод: nums = [2,1,-1]
# Вывод: 0

# Объяснение: 
# Опорный элемент - 0.
# Left sum = 0 (нет элементов левее индекса 0)
# Right sum = nums[1] + nums[2] = 1 + -1 = 0

# Решение задачи (https://telegra.ph/Nahozhdenie-opornogo-ehlementa-Reshenie-zadachi-08-15)
