#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2023
# 2023-03-18 2023-03-18 1.1 OK
# lc-submaxprod

import math

def solve(array: list[int]):
    """solve one task"""
    
    maxprod = None

    for i in range(len(array)):
        for j in range(i+1, len(array)):
            aprod = math.prod(array[i : j])
            if maxprod != None:
                if aprod > maxprod:
                    maxprod = aprod
            else:
                maxprod = aprod

    return maxprod


def test(array: list[int]) -> int:
    print(f"{array=} => {solve(array)}")


test([2, 3, -2, 4])
test([-2, 0, -1])


# Подмассив с наибольшим произведением

#  (https://leetcode.com/problems/maximum-product-subarray/)Сложность: Средняя 

# Условие задачи: на вход подается массив из чисел, необходимо вычислить максимальное произведение, которое встречается в подмассиве исходного массива. 

# Подмассив - последовательный кусок исходного массива.

# Пример:

# Ввод: nums = [2,3,-2,4]
# Вывод: 6
# Объяснение: [2, 3] имеют наибольшее произведение.

# Ввод: nums = [-2,0,-1]
# Вывод: 0
