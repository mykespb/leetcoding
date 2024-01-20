#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2023
# lc-index1.py 2024-01-19 2024-01-19 1.0 ver.2

def solve(haystack: str, needle: str) -> list[str]:
    """solve 1 task"""
   
    return haystack.find(needle)


def test(haystack: str, needle: str) -> None: 
    """ show """
    
    print(f"{haystack=}, {needle=} -> {solve(haystack, needle)}")


test(haystack = "sadbutsad", needle = "sad")
test(haystack = "sadbutsad", needle = "but")
test(haystack = "leetcode", needle = "leeto")

# haystack='sadbutsad', needle='sad' -> 0
# haystack='sadbutsad', needle='but' -> 3
# haystack='leetcode', needle='leeto' -> -1

# Нахождение индекс первого вхождения в строку

#  (https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)
    
# Сложность: Средняя 

# Условие задачи: дается две строки needle и haystack, верните индекс первого появления иглы в стоге сена или -1, если игла не является частью стога сена.

# Пример:

# Ввод: haystack = "sadbutsad", needle = "sad"
# Вывод: 0

# Ввод: haystack = "leetcode", needle = "leeto"
# Вывод: -1