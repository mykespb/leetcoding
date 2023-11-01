#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2023
# 2023-03-10 2023-03-10 1.0

def solve(arr, minK, maxK):
    """найти количество подмассивов"""

    la = len(arr)   # array length
    nosa = 0        # number of subarrays

    for left in range(la):
        for right in range(left+1, la+1):
            if min(arr[left:right]) == minK and max(arr[left:right]) == maxK:
                nosa += 1
                # print(f"{nosa=}, {left=}, {right=}, arr={arr[left:right]}")

    return nosa

# tests

nums = [1, 3, 5, 2, 7, 5]
minK = 1
maxK = 5

print(f"{nums=}, {minK=}, {maxK=}")
print("result:", solve(nums, minK, maxK))

nums = [1, 1, 1, 1]
minK = 1
maxK = 1

print(f"{nums=}, {minK=}, {maxK=}")
print("result:", solve(nums, minK, maxK))


# Подмассив с фиксированными границами

#  (https://leetcode.com/problems/count-subarrays-with-fixed-bounds/description/)
# Сложность: Тяжёлая

# Условие задачи: дается целочисленный массив nums и два целых числа minK и maxK.

# Подмассив nums с фиксированной привязкой - это подмассив, который удовлетворяет следующим условиям:

# Минимальное значение в подмассиве равно minK.
# Максимальное значение в подмассиве равно max.
# Возвращает количество подмассивов с фиксированной привязкой.

# Подмассив - это непрерывная часть массива.

# Пример:

# Ввод: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
# Вывод: 2

# Ввод: nums = [1,1,1,1], minK = 1, maxK = 1
# Вывод: 10

# Замечание. В условии задачи опечатка: надо не max, а maxK.

# myke/pro/leetcoding/lc-fixlim.py 
# nums=[1, 3, 5, 2, 7, 5], minK=1, maxK=5
# result: 2
# nums=[1, 1, 1, 1], minK=1, maxK=1
# result: 10
