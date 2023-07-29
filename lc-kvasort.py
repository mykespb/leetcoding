#!/usr/bin/env python
# Mikhail Kolodin
# lc-kvasort.py 2023-07-29 2023-07-29 2.0

def solve1(nums):
    """solve 1 task, 1st method, O(n log n)"""
    return sorted(map(lambda x: x*x, nums))

def solve2(nums):
    """solve 1 task, 2nd method, O(n)"""
    res = []
    left = 0
    right = len(nums)-1
    while left <= right:
        le = abs(nums[left])
        re = abs(nums[right])
        if le > re:
            res += [le*le]
            left += 1
        else:
            res += [re*re]
            right -= 1
    res.reverse()
    return res

def test(nums):
    """run 1 test"""
    print(f"{nums=} => {solve1(nums)}, {solve2(nums)}")

test(nums = [-4,-1,0,3,10])
test(nums = [-7,-3,2,3,11])

# nums=[-4, -1, 0, 3, 10] => [0, 1, 9, 16, 100], [0, 1, 9, 16, 100]
# nums=[-7, -3, 2, 3, 11] => [4, 9, 9, 49, 121], [4, 9, 9, 49, 121]

# Квадраты отсортированного массива (https://leetcode.com/problems/squares-of-a-sorted-array/)

# Сложность: Лёгкая

# Условие задачи: дан массив, отсортированный в порядке неубывания. Надо вернуть массив (также отсортированный), состоящий из элементов первого массива, возведенных во вторую степень. 

# Пример:

# Ввод: nums = [-4,-1,0,3,10]
# Вывод: [0,1,9,16,100]
# Объяснение: после возведения в квадрат получаем следующий массив - [16,1,0,9,100], а результирующий будет выглядеть следующим образом - 0,1,9,16,100]. 

# Ввод: nums = [-7,-3,2,3,11]
# Вывод: [4,9,9,49,121]

# Решить задачу надо за линейное время. 
