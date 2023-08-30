#!/usr/bin/env python
# Mikhail Kolodin
# lc-uparray.py 2023-08-30 2023-08-30 1.0

from itertools import compress


def solve(nums: list[int]) -> set:
    """solve 1 task"""

    lnums = len(nums)
    assert lnums > 1

    sols = set()

    for n in range(3, 2**lnums):
        pattern = [int(x) for x in list(f"{n:0{lnums}b}")]
        suba = list(compress(nums, pattern))

        if len(suba) > 1 and uping(suba):
            suba = tuple(sorted(suba))
            sols |= {suba}

    return sols


def uping(arr: list[int]) -> bool:
    """yes if array goes up"""

    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
        
    return True


def test(nums: list[int]) -> None:
    """run 1 test"""

    print(f"{nums=} => {solve(nums)}")    

test(nums = [4,6,7,7])
test(nums = [4,4,3,2,1])

# nums=[4, 6, 7, 7] => {(6, 7), (7, 7), (6, 7, 7), (4, 7, 7), (4, 6, 7, 7), (4, 6), (4, 7), (4, 6, 7)}
# nums=[4, 4, 3, 2, 1] => {(4, 4)}


# Неубывающий подмассив

#  (https://leetcode.com/problems/non-decreasing-subsequences/)Сложность: Средняя 

# Условие задачи: дается целочисленный массив nums, верните все различные возможные неубывающие подпоследовательности данного массива, по крайней мере, с двумя элементами. Вы можете вернуть ответ в любом порядке.

# Пример:

# Ввод: nums = [4,6,7,7]
# Вывод: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

# Ввод: nums = [4,4,3,2,1]
# Вывод: [[4,4]]