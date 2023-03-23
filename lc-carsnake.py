#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2023
# 2023-03-23 2023-03-23 0.2 in process
# lc-carsnake.py

def carfleet(target: int, position: list[int], speed: list[int]) -> int:
    pair = [(p, s) for p, s in zip(position, speed)]
    pair.sort(reverse=True)
    stack = []

    for p, s in pair:
        stack.append((target - p) / s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    
    return len(stack)


def test(target, position, speed):
    """make 1 test"""
    print(f"task: {target=}, {position=}, {speed=}\ncarfleet: {carfleet(target, position, speed)}\n")

# tests
test(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3])
test(10, [3], [3])
test(10, [1, 2], [30, 1])


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

# Змейка из машин. Решение задачи.
# November 17, 2022
# Для решения данной задачи необходимо посчитать оставшееся время в пути для каждой машины, а после сгруппировать по этому времени. 
