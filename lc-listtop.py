#!/usr/bin/env python
# Mikhail Kolodin
# lc-listtop.py 2023-10-04 2023-10-04 1.0


def solve(nums: list[int]) -> int:
    """solve 1 task"""

    start  = 0
    finish = len(nums)-1

    while start < finish:

        cur = (finish + start) // 2

        if nums[cur] < nums[cur+1]:
            start = cur + 1
        else:
            finish = cur
    
    return finish


def test(nums: list[int]) -> None:
    """run 1 test"""

    print(f"{nums=} => {solve(nums)}")    


test(nums = [1,2,3,1])
test(nums = [1,2,1,3,5,6,4])


# nums=[1, 2, 3, 1] => 2
# nums=[1, 2, 1, 3, 5, 6, 4] => 5


# Нахождение вершины списка

#  (https://leetcode.com/problems/find-peak-element/)Сложность: Средняя 

# Условие задачи: вершина списка - элемент, который больше как соседа слева, так и соседа справа.

# Дается целочисленный массив (проиндексированный с 0), необходимо вычислить элемент, который является вершиной списка, а после вернуть его индекс. В случае нескольких таких элементов можно вернуть любой из вариантов.

# Алгоритм должен иметь временную сложность O (log n).

# Пример:

# Ввод: nums = [1,2,3,1]
# Вывод: 2 

# Ввод: nums = [1,2,1,3,5,6,4]
# Вывод: 5
