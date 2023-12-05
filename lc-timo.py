#!/usr/bin/env python

# Mikhail Kolodin
# lc-timo.py 2023-12-01 2023-12-01 1.1

def solve(timeSeries, duration) -> int:
    """solve problem"""

    ill = set()

    for tempo in timeSeries:
        for dura in range(duration):
            ill |= {tempo + dura}

    return len(ill)


def test(timeSeries, duration) -> None:
    """run 1 test"""

    assert len(timeSeries)
    assert duration > 0

    print(f"{timeSeries=}, {duration=} =>", solve(timeSeries, duration))

test(timeSeries = [1,4], duration = 2)

# Атака Тимо

#  (https://leetcode.com/problems/teemo-attacking/description/)
# Сложность: Лёгкая

# Условие задачи: происходит абстрактная ситуация наш персонаж Тимо атакует своего соперника Эша. Результатом атаки является отравление оппонента на duration секунд. То есть начав атаку в момент времени t отравление будет длиться в промежуток времени [t, t + duration - 1]. 

# Если Тимо решит нанести ещё один удар до окончания действия отравления от предыдущего, то итоговое отравление закончится через duration секунд. 

# На вход подаётся массив из моментов времени нападений, а также длительность действия яда. Необходимо вычислить суммарную длительность действия отравы. 

# Пример:

# Ввод: timeSeries = [1,4], duration = 2
# Вывод: 4
