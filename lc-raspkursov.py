#!/usr/bin/env python
# Mikhail Kolodin
# lc-raspkursov.py 2023-07-27 2023-07-27 1.0

from itertools import permutations as gen

def solve(numCourses, prerequisites):
    starters = [x for x in range(numCourses) if x not in [y[0] for y in prerequisites]]
    enders = [x for x in range(numCourses) if x in [y[0] for y in prerequisites]]

    for comb in gen(enders):
        tested = starters + list(comb)

        for test in prerequisites:
            if tested.index(test[0]) < tested.index(test[1]):
                break
        else:
            return tested


def test(numCourses, prerequisites):
    print(f"{numCourses=}, {prerequisites=} => {solve(numCourses, prerequisites)}\n")

test(numCourses = 2, prerequisites = [[1,0]])
test(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]])

# numCourses=2, prerequisites=[[1, 0]] => [0, 1]

# numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]] => [0, 1, 2, 3]

# Расписание курсов

#  (https://leetcode.com/problems/course-schedule-ii/)Сложность: Средняя

# Условие задачи: дается количество курсов, сами курсы пронумерованны с нуля. Помимо этого дан массив, в котором хранятся зависимости. Зависимость 
# prerequisites[i] = [ai, bi] предполагает, что курс ai может быть пройден только в случае, если пройден курс bi. 

# Ответ на задачу должен содержать в себе такую последовательность курсов, при которой все курсы будут пройдены. 

# Если невозможно осуществить проход по всем курсам, то в ответе надо вывести пустой массив. 

# Пример:

# Ввод: numCourses = 2, prerequisites = [[1,0]]
# Вывод: [0,1]
# Объяснение: чтобы пройти все курсы, изначально надо пройти курс под номером "0", а после имеется возможность пройти курс под номером "1". 

# Ввод: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Вывод: [0,2,1,3]
