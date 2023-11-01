#!/usr/bin/env python

# Mikhail Kolodin, 2023-04-22
# lc-idealnum.py 2023-04-22 2023-04-22 0.1

def check(num: int) -> bool:
    """проверить данное число"""
    
    if num < 2:
        return False

    divs = []
    for dn in range(1, num):
        if num % dn == 0:
            divs.append(dn)

    if sum(divs) == num:
        print(num, "-> true")
    else:
        print(num, "-> false")


# tests

check(28)
check(7)

# 28 -> true
# 7 -> false

# Идеальное число

#  (https://leetcode.com/problems/perfect-number/description/)
# Сложность: Лёгкая

# Условие задачи: идеальное число - это положительное целое число, которое равно сумме делителей этого же числа, за исключением самого числа.

# Необходимо проверить входное число на идеальность.

# Пример:

# Ввод: num = 28
# Вывод: true
# Объяснение: 28 = 1 + 2 + 4 + 7 + 14

# Ввод: num = 7
# Вывод: false
