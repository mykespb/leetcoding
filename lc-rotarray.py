#!/usr/bin/env python

# Mikhail Kolodin
# lc-rotarray.py 2023-05-30 2023-05-30 1.0

class BadData (Exception): pass

def rotarray (nums: list[int], k: int) -> list[int]:
    """rotate it"""

    if k == 0:
        return nums
    if k < 0:
        raise BadData
    
    return nums[-k:] + nums[:-k]
    

print(rotarray([1, 2, 3, 4, 5, 6, 7], 3))
print(rotarray([-1, -100, 3, 99], 2))

print(rotarray([11, 22, 33], 0))
print(rotarray([11, 22, 33], -1))

# Сместить (https://leetcode.com/problems/rotate-array/) массив

#  (https://leetcode.com/problems/rotate-array/)
# Сложность: Средняя

# Условие задачи: дан массив, необходимо сместить массив на k-элементов, где k - неотрицательное число. 

# Пример:

# Ввод: nums = [1,2,3,4,5,6,7], k = 3
# Вывод: [5,6,7,1,2,3,4]

# Ввод: nums = [-1,-100,3,99], k = 2
# Вывод: [3,99,-1,-100]


# [5, 6, 7, 1, 2, 3, 4]
# [3, 99, -1, -100]
# [11, 22, 33]
# Traceback (most recent call last):
#   File "/home/myke/pro/leetcoding/./lc-rotarray.py", line 23, in <module>
#     print(rotarray([11, 22, 33], -1))
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/home/myke/pro/leetcoding/./lc-rotarray.py", line 14, in rotarray
#     raise BadData
# BadData
