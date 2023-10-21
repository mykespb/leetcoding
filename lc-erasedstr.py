#!/usr/bin/env python
# Mikhail Kolodin
# lc-erasedstr.py 2023-10-21 2023-10-21 1.0

def solve(s, t):
    """solve 1 task"""

    return proc(s) == proc(t)


def proc(s):
    """process 1 string"""

    if s == "":
        return s
    
    while (pos := s.find("#")) != -1:

        if pos == 0:
            s = s[1:]
        else:
            s = s[:pos-1] + s[pos+1:]

    return s


def test(s, t):
    """run 1 test"""

    print(f"\n{s=}, {t=} => {solve(s, t)}")

test(s = "ab#c", t = "ad#c")
test(s = "ab##", t = "c#d#")
test(s = "a#c", t = "b")

# s='ab#c', t='ad#c' => True

# s='ab##', t='c#d#' => True

# s='a#c', t='b' => False

# Сравнение стёртых строк 
# 
# (https://leetcode.com/problems/backspace-string-compare/)

# Сложность: Лёгкая 

# Условие задачи: даны две строки, необходимо выяснить являются они идентичными после удаления символов путем использования клавиши backspace (символ #). 

# Если строка пустая, то backspace оставляет её пустой. 

# Пример:

# Ввод: s = "ab#c", t = "ad#c"
# Вывод: true
# Объяснение: обе строки после использования удаления символов образуют сроку "ac"

# Ввод: s = "ab##", t = "c#d#"
# Вывод: true

# Ввод: s = "a#c", t = "b"
# Вывод: false

# Решение задачи (https://telegra.ph/Sravnenie-styortyh-strok-Reshenie-zadachi-10-07)

# (это сотая решённая задача на LeetCode ! :) )
