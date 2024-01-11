#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2023
# lc-maxavgsubarray.py 2024-01-11 2024-01-11 1.0

def solve(nums: list[int], k: int) -> float:
    """solve 1 task"""

    alen = len(nums)
    assert alen > 0
    assert k > 0
    assert alen >= k

    ms = sum(nums[:k]) / k
    for start in range(1, alen-k):
        ms = max(ms, sum(nums[start: start+k]) / k) 

    return ms


def test(nums: list[int], k: int) -> None: 
    """ show """
    
    print(f"{nums=}, {k=} -> {solve(nums, k)}")


test(nums = [1,12,-5,-6,50,3], k = 4)
test(nums = [5], k = 1)

# nums=[1, 12, -5, -6, 50, 3], k=4 -> 12.75
# nums=[5], k=1 -> 5.0

# Максимальное среднее подмассива

#  (https://leetcode.com/problems/maximum-average-subarray-i/description/)Сложность: Лёгкая

# Условие задачи: дается целочисленный массив nums, состоящий из n элементов и целого числа k.

# Найдите непрерывный подмассив, длина которого равна k, который имеет максимальное среднее значение, и верните это значение. Будет принят любой ответ с ошибкой вычисления менее 10-5.

# Пример:

# Ввод: nums = [1,12,-5,-6,50,3], k = 4
# Вывод: 12.75000
# Объяснение:

# Ввод:  nums = [5], k = 1
# Вывод: 5.00000
