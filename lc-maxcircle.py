#!/usr/bin/env python
# Mikhail Kolodin
# lc-mxcircle.py 2023-09-13 2023-09-13 1.1

# def solve(nums: list[int]) -> tuple[int]:
def solve(nums: list[int]) -> int:
    """solve 1 task"""

    lenn = len(nums)
    assert lenn > 0

    msum = nums[0]
    mkol = 1
    
    for start in range(lenn):
        for kol in range(lenn):

            asum = summa(nums, start, kol)
            if asum > msum:

                msum = asum
                mstart = start
                mkol = kol

    return msum
    # return msum, mstart, mkol


def summa(nums: list[int], start: int, kol:int) -> int:
    """count current sum"""

    lenn = len(nums)
    tsum = 0
    for i in range(kol):
        tsum += nums[(start + i) % lenn]

    return tsum


def test(nums: list[int]) -> None:
    """run 1 test"""

    print(f"{nums=} => {solve(nums)}")    


test(nums = [1,-2,3,-2])
test(nums = [5,-3,5])

# nums=[1, -2, 3, -2] => 3
# nums=[5, -3, 5] => 10

# nums=[1, -2, 3, -2] => (3, 2, 1)
# nums=[5, -3, 5] => (10, 2, 2)


# Максимальная сумма замкнутого подмассива

#  (https://leetcode.com/problems/maximum-sum-circular-subarray/)Сложность: Средняя 

# Условие задачи: дается круговой целочисленный массив nums длины n, верните максимально возможную сумму непустого подмассива nums.

# Циклический массив означает, что конец массива соединяется с началом массива. Формально следующим элементом nums[i] является nums[(i + 1) % n], а предыдущим элементом nums[i] является nums[(i - 1 + n) % n].

# Подмассив может включать в себя каждый элемент фиксированных чисел буфера не более одного раза. Формально, для подмассива nums[i], nums[i + 1], ..., nums[j] не существует i <= k1, k2 <= j с k1 % n == k2 % n.

# Пример:

# Ввод: nums = [1,-2,3,-2]
# Вывод: 3
# Объяснение: [3]

# Ввод: nums = [5,-3,5]
# Вывод: 10