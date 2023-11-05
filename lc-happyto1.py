#!/usr/bin/env python
# Mikhail Kolodin
# lc-happyto1.py 2023-11-04 2023-11-04 1.1

def solve(n: int) -> bool:
    """solve 1 task"""

    was = set()

    while n not in was and n != 1:
        was.add(n)
        n = sum( map( lambda x: x*x, map( int, list( str(n) ) ) ) )

        # digs = map( int, list(str(n)) ) 
        # n = sum( map( lambda x: x*x, digs) )
        # print(f"{n=}")

    return n == 1


def test(n: int) -> None:
    """run 1 test"""

    print(f"{n=} => {solve(n)}")    

test(n = 19)
test(n = 2)

# n=19 => True
# n=2 => False

# n=82
# n=68
# n=100
# n=1
# n=19 => True

# n=4
# n=16
# n=37
# n=58
# n=89
# n=145
# n=42
# n=20
# n=4
# n=2 => False

# Счастливое число

#  (https://leetcode.com/problems/happy-number/)
# Сложность: Лёгкая

# Условие задачи: требуется написать алгоритм, определяющий является ли число счастливым. 

# Счастливым называется число, соответствующее следующим требованиям:
# - создается число, являющееся суммой квадратов цифр числа на предыдущей итерации;
# - процесс прододжается до тех пор, пока данная сумма не будет равна 1 или не зациклится;
# - числа, которые сходяится по данному алгаритму к единице и являются счастливыми. 

# Пример:

# Ввод: n = 19
# Вывод: true
# Объяснение: 
# 1 + 81 = 82
# 64 + 4 = 68
# 36 + 64 = 100
# 1 + 0 + 0 = 1

# Ввод: n = 2
# Вывод: false
