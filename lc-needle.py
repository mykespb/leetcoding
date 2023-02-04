#!/usr/bin/env python
# Mikhail Kolodin, 2023
# 2023-02-04 2023-02-04 1.0

def isin(n, h):
    if n not in h:
        return -1

    nl = len(n)

    for pos in range(len(h) - nl):
        if h[pos: pos+ nl] == n:
            return pos

haystack = "sadbutsad"
needle = "sad"

print(needle, haystack, isin(needle, haystack))

haystack = "leetcode"
needle = "leeto"

print(needle, haystack, isin(needle, haystack))

haystack = "leetcodeleetooni"
needle = "leeto"

print(needle, haystack, isin(needle, haystack))


# ~ Нахождение индекс первого вхождения в строку

 # ~ (https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)Сложность: Средняя 

# ~ Условие задачи: дается две строки needle и haystack, верните индекс первого появления иглы в стоге сена или -1, если игла не является частью стога сена.

# ~ Пример:

# ~ Ввод: haystack = "sadbutsad", needle = "sad"
# ~ Вывод: 0

# ~ Ввод: haystack = "leetcode", needle = "leeto"
# ~ Вывод: -1

# ~ Решение задачи (https://telegra.ph/Nahozhdenie-indeks-pervogo-vhozhdeniya-v-stroku-Reshenie-zadachi-02-04)
