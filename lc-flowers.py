#!/usr/bin/env python
# Mikhail Kolodin
# lc-flowers.py 2023-09-10 2023-09-10 1.0

def solve(flowerbed: list[int], n: int) -> bool:
    """solve 1 task"""

    flen = len(flowerbed)
    assert flen > 0
    assert n >= 0

    if n == 0:
        return True

    if flen == 1 and flowerbed[0] == 0 and n == 1:
        return True

    done = 0

    for pos in range(flen):

        if pos == 0 and flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[1] = 1
            done += 1
            if done == n:
                return True

        if pos == flen-1 and flowerbed[pos] == 0 and flowerbed[pos-1] == 0:
            flowerbed[pos] = 1
            done += 1
            if done == n:
                return True

        if pos>0 and pos<flen-1 and sum(flowerbed[pos-1:pos+2]) == 0:
            flowerbed[pos] = 1
            done += 1
            if done == n:
                return True

    return False


def test(flowerbed: list[int], n: int) -> None:
    """run 1 test"""

    print(f"{flowerbed=}, {n=} => {solve(flowerbed, n)}")    


test(flowerbed = [1,0,0,0,1], n = 1)
test(flowerbed = [1,0,0,0,1], n = 2)
test(flowerbed = [0,0,0,0,0], n = 3)
test(flowerbed = [1,1,1,1,1], n = 3)

# flowerbed=[1, 0, 0, 0, 1], n=1 => True
# flowerbed=[1, 0, 0, 0, 1], n=2 => False
# flowerbed=[0, 0, 0, 0, 0], n=3 => False
# flowerbed=[1, 1, 1, 1, 1], n=3 => False


# Усадка клумбы

#  (https://leetcode.com/problems/can-place-flowers/)Сложность: Лёгкая

# Условие задачи: есть длинная клумба, на которой некоторые участки засажены, а некоторые нет. Однако цветы нельзя сажать на соседних участках.

# Учитывая целочисленный массив flowerbed, содержащий 0 и 1, где 0 означает пустой, а 1 означает непустой, и целое число n, верните, если на клумбе можно посадить n новых цветов, не нарушая правила отсутствия соседних цветов.

# Пример:

# Ввод: flowerbed = [1,0,0,0,1], n = 1
# Вывод: true

# Ввод: flowerbed = [1,0,0,0,1], n = 2
# Вывод: false
