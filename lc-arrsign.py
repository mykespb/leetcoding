#!/usr/bin/env python

# Mikhail Kolodin
# lc-arrsign.py 2023-06-15 2023-06-15 1.0

def solve1(arr: list[int]) -> int:
    """sign of array"""

    if 0 in arr: return 0
    return 1 if len( list(filter(lambda x: x<0, arr)) ) % 2 == 0 else -1

def signFunc(n: int) -> int:
    """sign -- not used"""

    return 0 if n==0 else 1 if n>0 else -1

def test(arr):
    """print test results"""

    print(f"task: {arr=},\nresult: {solve(arr)}")

test([-1, -2, -3, -4, 3, 2, 1])
test([1, 5, 0, 2, -3])

# Знак произведения массива

#  (https://leetcode.com/problems/sign-of-the-product-of-an-array/)Сложность задачи: Легкая

# Условие задачи:
# Существует функция signFunc(x), которая возвращает:
#     1, если x положительно
#     -1, если x отрицательно
#     0, если x равно 0.
# Вам дается целочисленный массив nums. Пусть product - это произведение всех значений в массиве nums. Верните signFunc(product).

# Пример:
# Ввод: nums = [-1,-2,-3,-4,3,2,1]
# Вывод: 1
# Объяснение: Произведение всех значений в массиве равно 144, а signFunc(144) = 1.

# Ввод: nums = [1,5,0,2,-3]
# Вывод: 0
