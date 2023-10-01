#!/usr/bin/env python
# Mikhail Kolodin
# lc-longones.py 2023-10-01 2023-10-01 1.0


def solve(nums):
    """solve 1 task"""

    ingroup = False
    maxsum = 0
    asum = 0

    for val in nums:
        if val:
            if ingroup:
                asum += 1
                maxsum = max(maxsum, asum)
            else:
                ingroup = True
                asum = 1
                maxsum = max(maxsum, asum)
        else:
            ingroup = False
                
    return maxsum


def test(nums):
    """run 1 test"""

    print(f"{nums=} => {solve(nums)}")    

test(nums = [1,1,0,1,1,1])
test(nums = [1,1,0,1,1,1, 0, 0])
test(nums = [1])
test(nums = [0])

# nums=[1, 1, 0, 1, 1, 1] => 3
# nums=[1, 1, 0, 1, 1, 1, 0, 0] => 3
# nums=[1] => 1
# nums=[0] => 0


# Максимальное количество единиц

#  (https://leetcode.com/problems/max-consecutive-ones/)Сложность: Лёгкая 

# Условие задачи: дается бинарный массив (состоит только из 0 и 1). Необходимо вычислить максимальную длину подмассива, в котором присутствуют только 1. 

# Пример:

# Ввод: nums = [1,1,0,1,1,1]
# Вывод: 3