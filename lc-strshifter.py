#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2023
# lc-strshifter.py 2024-01-14 2024-01-14 1.0

def solve(s: str, goal: str) -> bool:
    """solve 1 task"""

    s = list(s)
    g = list(goal)

    for _ in range(len(s)):
        if s == g:
            return True
        s = s[1:] + s[:1]

    return False

def test(s: str, goal: str) -> None: 
    """ show """
    
    print(f"{s=}, {goal=} -> {solve(s, goal)}")


test(s = "abcde", goal = "cdeab")
test(s = "abcde", goal = "abced")

# s='abcde', goal='cdeab' -> True
# s='abcde', goal='abced' -> False

# Строка-перевертыш

#  (https://leetcode.com/problems/rotate-string/)

# Сложность: Лёгкая

# Условие задачи: дается две строки s и goal, верните true тогда и только тогда, когда s может стать goal после некоторого количества смен в субботу.

# Сдвиг на s состоит в перемещении крайнего левого символа s в крайнюю правую позицию.

# Например, если s = "abcde", то после одной смены это будет "bcdea".

# Пример:

# Ввод: s = "abcde", goal = "cdeab"
# Вывод: true

# Ввод:  s = "abcde", goal = "abced"
# Вывод: false