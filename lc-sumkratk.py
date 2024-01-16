#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2023
# lc-sumkratk.py 2024-01-15 2024-01-15 1.0

def solve(nums, k):
    """solve 1 task"""

    assert k > 0
    assert len(nums) > 0

    cnt = 0

    for start in range(len(nums)):
        for finish in range(start+1, len(nums)+1):
            if sum(nums[start:finish]) % k == 0:
                cnt += 1

    return cnt

def test(nums, k): 
    """ show """
    
    print(f"{nums=}, {k=} -> {solve(nums, k)}")


test(nums = [4,5,0,-2,-3,1], k = 5)
test(nums = [5], k = 9)

# nums=[4, 5, 0, -2, -3, 1], k=5 -> 7
# nums=[5], k=9 -> 0

# Суммы подмассивов, кратные K

# (https://leetcode.com/problems/subarray-sums-divisible-by-k/)
# Сложность: Средняя 

# Условие задачи: дается целочисленный массив nums и целое число k, верните количество непустых подмассивов, сумма которых делится на k.

# Подмассив - это непрерывная часть массива.

# Пример:

# Ввод: nums = [4,5,0,-2,-3,1], k = 5
# Вывод: 7
# Объяснение: [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

# Ввод: nums = [5], k = 9
# Вывод: 0
