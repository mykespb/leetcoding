#!/usr/bin/env python
# Mikhail Kolodin
# lc-intersectint.py 2023-10-09 2023-10-09 1.0

def solve(ints, nint):
    """solve 1 task"""

    ints.append(nint)
    ints.sort()

    pos = 0

    while pos < len(ints)-1:
        if ints[pos][1] >= ints[pos+1][0]:
            ints[pos][1] = max( ints[pos][1], ints[pos+1][1] )
            del ints[pos+1]
        else:
            pos += 1

    return ints

def test(ints, nint):
    """run 1 test"""

    print(f"\n{ints=}, {nint=} => {solve(ints, nint)}")    


test(ints = [[1,3],[6,9]], nint = [2,5])
test(ints = [[1,2],[3,5],[6,7],[8,10],[12,16]], nint = [4,8])

# ints=[[1, 3], [6, 9]], nint=[2, 5] => [[1, 5], [6, 9]]
# ints=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], nint=[4, 8] => [[1, 2], [3, 10], [12, 16]]


# Пересечение интервала

#  (https://leetcode.com/problems/insert-interval/)
# Сложность: Средняя 

# Условие задачи: дается массив из непересекающихся интервалов, где первое число подсписка - начальная координата, а второе число - конечная координата. Также подается новый интервал.

# Необходимо внедрить новый интервал в уже существующий список и вернуть полученный результат после вставки.

# Пример:

# Ввод: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Вывод: [[1,5],[6,9]]

# Ввод: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Вывод:  [[1,2],[3,10],[12,16]]