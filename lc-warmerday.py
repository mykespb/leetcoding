#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2023
# lc-warmerday.py 2023-12-12 2023-12-12 1.0

def solve(temperatures: list[int]) -> list[int]:
    """find max subarray"""

    res = []
    
    for i in range(len(temperatures)):
        for j in range(i+1, len(temperatures)):
            if temperatures[j] > temperatures[i]:
                res.append(j-i)
                break
        else:
            res.append(0)

    return res

def test(temperatures: list[int]) -> None: 
    """ show """
    
    print(f"{temperatures=} -> {solve(temperatures)}")


test(temperatures = [73,74,75,71,69,72,76,73])
test(temperatures = [30,40,50,60])

# temperatures=[73, 74, 75, 71, 69, 72, 76, 73] -> [1, 1, 4, 2, 1, 1, 0, 0]
# temperatures=[30, 40, 50, 60] -> [1, 1, 1, 0]


# Ежедневная температура (https://leetcode.com/problems/daily-temperatures/)

# Сложность: Средняя 

# Условие задачи: дается массив, в котором содержатся на температуры за определенный день. Необходимо вернуть массив, такой что будет содержать на i-ой позиции количество дней, которое необходимо выждать, чтобы наступил день теплее. Если такой ситуации не случается, то на i-ой позиции установить 0.

# Пример:

# Ввод:  temperatures = [73,74,75,71,69,72,76,73]
# Вывод: [1,1,4,2,1,1,0,0]

# Ввод: temperatures = [30,40,50,60]
# Вывод: [1,1,1,0]
