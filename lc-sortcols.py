#!/usr/bin/env python
# Mikhail Kolodin
# lc-sortcols.py 2023-09-03 2023-09-03 1.0

def solve(strs: list[str]) -> int:
    """solve 1 task"""

    assert (lena := len(strs)) and len(strs[0])

    todel = 0 
    col = 0    

    while col < len(strs[0]):

        if not good(strs, col):
            todel += 1

            for line in range(lena):
                strs[line] = strs[line][:col] + strs[line][col+1:]

        else:
            col += 1

    return todel


def good(strs: list[str], col: int):
    """check if column col is well sorted"""

    seq = "" .join ([ strs[line][col] for line in range(len(strs)) ])
    return seq == "".join(sorted(seq))


def test(strs: list[str]) -> None:
    """run 1 test"""

    print(f"{strs=} => {solve(strs)}")    


test(strs = ["cba","daf","ghi"])
test(strs = ["a","b"])

# strs=['cba', 'daf', 'ghi'] => 1
# strs=['a', 'b'] => 0

# Сортировка столбцов

#  (https://leetcode.com/problems/delete-columns-to-make-sorted/)Сложность: Лёгкая

# Условие задачи: предоставляется массив из n строк strs, все одинаковой длины.

# Строки могут быть расположены таким образом, чтобы на каждой строке было по одной, образуя сетку. Например, strs = ["abc", "bce", "ce"] может быть организован как:

# abc
# bce
# cae

# Вам нужно удалить столбцы, которые не отсортированы лексикографически. В приведенном выше примере (с индексом 0) столбцы 0 ('a', 'b', 'c') и 2 ('c', 'e', 'e') отсортированы, в то время как столбец 1 ('b', 'c', 'a') не отсортирован., таким образом, вы бы удалили столбец 1.

# Верните количество столбцов, которые нужно удалять.

# Пример:

# Ввод: strs = ["cba","daf","ghi"]
# Вывод: 1

# Ввод: strs = ["a","b"]
# Вывод: 0
