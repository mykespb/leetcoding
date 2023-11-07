#!/usr/bin/env python
# Mikhail Kolodin
# lc-minof69.py 2023-09-28 2023-09-29 2.0


def solve1(num):
    """solve 1 task"""

    digs = list(str(num))

    if '6' in digs:

        pos = digs.index('6')
        nova = digs[:pos] + ['9'] + digs[pos+1:]

        out = int("".join(nova))
        return out

    else:
        return num


def solve2(num):
    """solve 1 task"""

    return (num if '6' not in (digs := list(str(num)))
        else int("".join(digs[:(pos := digs.index('6'))] + ['9'] + digs[pos+1:])) )


def test(num):
    """run 1 test"""

    print(f"{num=} => {solve1(num)}, {solve2(num)}")    

test(9669)
test(9996)
test(669)
test(9999)
test(96)
test(6)


# num=9669 => 9969, 9969
# num=9996 => 9999, 9999
# num=669 => 969, 969
# num=9999 => 9999, 9999
# num=96 => 99, 99
# num=6 => 9, 9


# Максимальное число из 6 и 9

#  (https://leetcode.com/problems/maximum-69-number/)
# Сложность: Лёгкая

# Условие задачи: дается число, полностью состоящее из 6 и 9. Необходимо вычислить наибольшее число в данной раскладке, при этом имея возможность заменить не более одной шестерки на девятку.

# Пример:

# Ввод: num = 9669
# Вывод: 9969

# Ввод: num = 9996
# Вывод: 9999

# Решение задачи (https://telegra.ph/Maksimalnoe-chislo-iz-6-i-9-Reshenie-zadachi-11-08)