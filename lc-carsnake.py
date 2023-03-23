#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2023
# 2023-03-23 2023-03-23 0.1 in process
# lc-carsnake.py

from dataclasses import dataclass

@dataclass
class Snake:
    number: int = 0
    speed: int = 0

def solve(target, position, speed) -> int:
    """solve 1 task"""

    # make road
    road = [Snake() for _ in range(target)]
    print(f"{road=}")

    # make initial state
    for c, s in zip(position, speed):
        road[c].number += 1
        road[c].speed = s    # TODO: thnk what is the order of cars
    print(f"{road=}")

    # run simulatuion
    ...

def test(target, position, speed):
    """make 1 test"""
    print(f"\ntask: {target=}, {position=}, {speed=}, answer: {solve(target, position, speed)}")

# tests
test(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3])
test(10, [3], [3])


# Змейка из машин

#  (https://leetcode.com/problems/car-fleet/)Сложность: Средняя  

# Условие задачи: есть n машин, направляющихся в одно и то же место на расстоянии target  по однополосной дороге.

# Дается два целочисленных массива длины n, в первом хранится положение, а во втором скорость соответствующей машины.

# Машины не могут обгонять друг друга, и в случае если быстрая машина догнала медленную, то движение она у же продолжает со скоростью медленной машины.

# Змейка из машин - группа нескольких или одной машины, достигающих одновременно целевого пункта (расстояние между машинами в одной змейке не учитывается).

# Необходимо вычислить количество таких змеек. 

# Пример:

# Ввод: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
# Вывод: 3
# Объяснение:

# Ввод: target = 10, position = [3], speed = [3]
# Вывод: 1

# Решение задачи (https://telegra.ph/Zmejka-iz-mashin-Reshenie-zadachi-11-17)
