#!/usr/bin/env python
# Mikhail Kolodin
# lc-icecosts.py 2023-09-01 2023-09-01 1.0

def solve(costs: list[int], coins: int) -> int:
    """solve 1 task"""

    costs.sort()
    got = 0

    for pos in range(len(costs)):
        if costs[pos] > coins:
            return got
        got += 1
        coins -= costs[pos]

    return 0


def test(costs: list[int], coins: int) -> None:
    """run 1 test"""

    print(f"{costs=}, {coins=} => {solve(costs, coins)}")    


test(costs = [1,3,2,4,1], coins = 7)
test(costs = [10,6,8,7,7,8], coins = 5)

# costs=[1, 3, 2, 4, 1], coins=7 => 4
# costs=[10, 6, 8, 7, 7, 8], coins=5 => 0


# Мороженое

#  (https://leetcode.com/problems/maximum-ice-cream-bars/description/)
# Сложность: Средняя

# Условие задачи: стоит душный летний день, и мальчик хочет купить несколько батончиков мороженого.

# В магазине есть n батончиков мороженого. Вам дается массив costs длины n, где costs[i] - это цена i-го батончика мороженого в монетах. У мальчика изначально есть монеты, которые можно потратить, и он хочет купить как можно больше батончиков мороженого. 

# Верните максимальное количество батончиков мороженого, которые мальчик может купить за монеты coins.

# Мальчик может купить батончики мороженого в любом порядке.

# Пример:

# Ввод: costs = [1,3,2,4,1], coins = 7
# Вывод: 4
# Объяснение:1 + 3 + 2 + 1 = 7.

# Ввод: costs = [10,6,8,7,7,8], coins = 5
# Вывод: 0