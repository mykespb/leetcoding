#!/usr/bin/env python

# Mikhail Kolodin
# lc-shares.py 2023-06-21 2023-06-21 1.0


def shares(prices: list[int]) -> int:
    """find bets shares purchase"""

    mv = 0
    for buy in range(len(prices) - 1):
        for sell in range(buy+1, len(prices)):
            if (better := prices[sell] - prices[buy]) > mv:
                mv = better

    return mv


def test(prices: list[int]) -> None:
    """print test results"""

    print(f'task: {prices}, result: {shares(prices)}')

test([7, 1, 5, 3, 6, 4])
test([7, 6, 4, 3, 1])

# task: [7, 1, 5, 3, 6, 4], result: 5
# task: [7, 6, 4, 3, 1], result: 0

# Лучшее время для покупки и продажи акций

#  (https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
# Условие задачи:
# Вам дан массив prices, где prices[i] — цена данной акции на i-й день.

# Вы хотите максимизировать свою прибыль, выбрав один день для покупки одной акции и выбрав другой день в будущем для продажи этой акции.

# Верните максимальную прибыль, которую вы можете получить от этой сделки. Если вы не можете получить никакой прибыли, верните 0.

# Пример:
# Ввод: prices = [7,1,5,3,6,4]
# Вывод: 5
# Объяснение: 
# Покупка во 2-й день (цена = 1) и продажа в 5-й день (цена = 6), прибыль = 6-1 = 5.
# Обратите внимание, что покупка во 2-й день и продажа в 1-й день не разрешены, потому что вы должны купить перед продажей.

# Ввод: prices = [7,6,4,3,1]
# Вывод: 0
