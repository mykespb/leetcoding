#!/usr/bin/env python
# Mikhail Kolodin
# lc-maxmidsub.py 2023-08-08 2023-09-08 1.2

def solve(nums: list[int], k: int):
    """solve complete task"""

    # eps = 1.e-5
    lnum = len(nums)

    assert k > 0
    assert lnum > 0

    ms = sum(nums[0:k]) / k

    for i in range(1, lnum-k+1):
        nav = sum(nums[i:i+k]) / k
        ms = max(ms, nav)

    return ms


def test(nums: list[int], k: int):
    """run 1 test"""
    print(f"task: {nums=}, {k=} => {solve(nums, k)}")

test([1, 12, -5, -6, 50, 3], 4)
test([5], 1)

# task: nums=[1, 12, -5, -6, 50, 3], k=4 => 12.75
# task: nums=[5], k=1 => 5

# можно было бы 
# diff = abs(sum(nums[i:i+k] / k))
# if diff <= eps: ...
# но незачем, 
# ибо ошибки могут быть при каждом вычислении,
# и нет причин считать одни лучше других.

# Максимальное среднее подмассива

#  (https://leetcode.com/problems/maximum-average-subarray-i/description/)
# 
# Сложность: Лёгкая

# Условие задачи: дается целочисленный массив nums, состоящий из n элементов и целого числа k.

# Найдите непрерывный подмассив, длина которого равна k, который имеет максимальное среднее значение, и верните это значение. Будет принят любой ответ с ошибкой вычисления менее 10-5.

# Пример:

# Ввод: nums = [1,12,-5,-6,50,3], k = 4
# Вывод: 12.75000
# Объяснение:

# Ввод:  nums = [5], k = 1
# Вывод: 5.00000