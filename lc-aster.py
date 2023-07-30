#!/usr/bin/env python
# Mikhail Kolodin
# lc-aster.py 2023-07-30 2023-07-30 1.0

def solve(asteroids):
    changed = True
    while changed:
        changed = False
        for i in range(len(asteroids) - 1):

            if asteroids[i] == -asteroids[i+1]:
                asteroids.pop()
                asteroids.pop()
                changed = True
                break

            if asteroids[i] > 0 and asteroids[i+1] < 0:
                if abs(asteroids[i]) > abs(asteroids[i+1]):
                    asteroids.pop(-1)
                else:
                    asteroids.pop(-2)
                changed = True
                break

    return asteroids


def test(asteroids):
    """run 1 test"""
    print(f"task: {asteroids=} => {solve(asteroids)}")

test(asteroids = [5,10,-5])
test(asteroids = [8,-8])

# task: asteroids=[5, 10, -5] => [5, 10]
# task: asteroids=[8, -8] => []

# Столкновение астероидов

#  (https://leetcode.com/problems/asteroid-collision/)Сложность: Средняя

# Условие задачи: дан массив астероидов (каждое значение - вес астероида, а знак - направление движения). Каждый из астероидов двигается с одинаковой скоростью. 

# При столкновени двух астероидов, асторид с меньшим весов уничтожается (у целого астероида вес остается неизменным после столкновения). 

# Вывести надо результирующий массив после всевозможных столкновений.  

# Пример:

# Ввод: asteroids = [5,10,-5] 
# Вывод: [5,10]
# Объяснение: 3-ий астероид сталкивается со 2-ым и уничтожается. 

# Ввод: asteroids = [8,-8]
# Вывод: [ ]
