#!/usr/bin/env python
# Mikhail Kolodin, 2023
# 2023-04-18 2023-04-18 1.0
# lc-near3sum.py 

from itertools import combinations

def solve(nums: list[int], target: int) -> int:
    """find nearest"""

    best = None
    bestvar = []
    for var in combinations(nums, 3):
        sumvar = sum(var)
        if not best or abs(sumvar - target) < best:
            best = sumvar
            bestvar = var

    return best, bestvar

# tests

print(solve([-1, 2, 1, -4], 1))
print(solve([0, 0, 0], 1))

# (2, (-1, 2, 1))
# (0, (0, 0, 0))

# Наиближайшая сумма трёх  (https://leetcode.com/problems/3sum-closest/)

# Сложность: Средняя

# Условие задачи: дан целочисленный массив и целевое значение суммы. Необходимо найти три числа из массива, которые либо в результате суммирования равны значению целевой суммы либо же максимально близки к ней по модулю. 

# Каждый массив имеет единственное решение. 

# Пример:

# Ввод: nums = [-1,2,1,-4], target = 1
# Вывод: 2
# Объяснение: (-1 + 2 + 1 = 2)

# Ввод: nums = [0,0,0], target = 1
# Вывод: 0

# Решение задачи (https://telegra.ph/Naiblizhajshaya-summa-treh-Reshenie-zadachi-10-20)
