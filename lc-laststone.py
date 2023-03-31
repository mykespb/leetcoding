#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2023
# 2023-03-31 2023-03-31 1.1 OK
# lc-laststone.py

def solve(array: list[int]) -> int:
    """solve 1 task"""
    
    if len(array) < 1:
        return 0
    
    while len(array) > 1:
        array.sort(reverse=True)

        if array[0] == array[1]:
            array = array[2:]
        else:
            array = [abs(array[0] - array[1])] + array[2:]
        
    if len(array):
        return array[0]
    else:
        return 0

def test(array: list[int]):
    """run a test"""
    print(f"{array=} => {solve(array)}")

test([2, 7, 4, 1, 8, 1])

# array=[2, 7, 4, 1, 8, 1] => 1

# Последний из камней

#  (https://leetcode.com/problems/last-stone-weight/)Сложность: Лёгкая 

# Условие задачи: на вход подается массив из камней, где i-ый элемент обозначает вес соответствующего камня.

# Осуществляется игра в камни: берутся два камня с наибольшим весом и сталкиваются. Результат их столкновения может быть следующим:

# - оба уничтожаются при условии одинакового веса;
# - при условии неравенства весов из веса большего вычитается меньший вес, а после снова добавляется в массив.

# Игра продолжается до тех пор пока есть хотя бы один камень,  необходимо вернуть это самый последний вес. При отсутствии камней в конце - вернуть ноль.

# Пример:

# Ввод: stones = [2,7,4,1,8,1]
# Вывод: 1
