#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2023
# 2023-04-03 2023-04-03 1.0
# lc-msga.py

def msga(s: str) -> str:
    """make string great again"""

    if len(s) < 2:
        return s
    
    need = True
    while need:
        need = False
        for ix in range(1, len(s)):
            if s[ix-1].islower() and s[ix] == s[ix-1].upper() or \
                s[ix-1].isupper() and s[ix] == s[ix-1].lower():
                need = True
                s = s[:ix-1] + s[ix+1:]
                break

    return s

def test(s: str) -> str:
    """run a test"""
    
    print(f"input:  {s}\noutput: {msga(s)}\n")

test("leEeetcode")

# input:  leEeetcode
# output: leetcode

# Make the string great AGAIN (https://leetcode.com/problems/make-the-string-great/)

# Сложность: Лёгкая 

# Условие задачи: дается строка, состоящая из латинских букв как в нижнем, так и в вернем регистре.

# Строка считается качественной, если две соседние буквы не представлены одной и той же буквой, но в разных регистрах. Такие буквы удаляются до тех пор, пока строка не станет качественной. 

# Вернуть надо строку, над которой были совершены все преобразования. Гарантируется уникальность ответа. 

# Пустая строка по умолчанию является качественной. 

# Пример:

# Ввод: s = "leEeetcode"
# Вывод: "leetcode"
