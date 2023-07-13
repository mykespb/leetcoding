#!/usr/bin/env python

# Mikhail Kolodin
# lc-confhalls.py 2023-07-12 2023-07-13 1.2

def solve(intervals: list[list[int, int]]) -> int:
    """solve problem"""

    events = sorted(
        [(when, 'start') for when, _ in intervals] +
        [(when, 'end') for _, when in intervals]
    )

    cur_rooms = max_rooms = 0

    for when, what in events:
        if what == 'start':
            cur_rooms += 1
            max_rooms = max(max_rooms, cur_rooms)
        else:
            cur_rooms -= 1

    return max_rooms

def test(intervals: list[list[int, int]]) -> None:
    """run 1 test"""

    print(intervals, solve(intervals))

test([[0, 30], [5, 10], [15, 20]])
test([[7, 10], [2, 4]])

test([[1, 2], [2, 4], [4, 5]])
test([])

# Конференц-залы II (https://leetcode.com/problems/meeting-rooms-ii/)

# Сложность задачи: Средняя

# Условие задачи:
# Дан массив интервалов времени проведения совещаний, intervals, где intervals[i] = [start(i), end(i)]. Найдите минимальное требуемое количество конференц-залов.

# Пример:
# Ввод: intervals = [[0,30],[5,10],[15,20]]
# Вывод: 2

# Ввод: intervals = [[7,10],[2,4]]
# Вывод: 1

# Примечание по решению: важно, что лексикографически 'end' раньше, чем 'start', 
# в результате мы сначала завершаем совещания, а потом начинаем новые, 
# что позволяет переиспользовать те же конференц-залы.
