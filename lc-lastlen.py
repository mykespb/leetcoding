#!/usr/bin/env python
# Mikhail Kolodin
# lc-lastlen.py 2023-08-23 2023-08-23 1.0

def solve1(s: str) -> int:
    """solve complete task"""
    
    return len(s.strip().split()[-1])
    

def solve2(s: str) -> int:
    """solve complete task"""
    
    state = 0
    spos = -1
    for pos in range(len(s)-1, -1, -1):
        if s[pos] == " ":
            if state == 1:
                return cpos - pos
        else:
            if state == 0:
                cpos = pos
                state = 1

    return cpos+1
    
    
def test(s: str) -> None:
    """run 1 test"""

    print(f"{s=} => {solve1(s)}, {solve2(s)}")    

test(s = "Hello World")
test(s = "   fly me   to   the moon  ")
test(s = "Hello")
test(s = "Hello                      ")
test(s = "                       Hello                      ")
test(s = "                       Hello")

# s='Hello World' => 5, 5
# s='   fly me   to   the moon  ' => 4, 4


# Длина последнего слова в строке

# Частота встречи задач на собеседованиях за последние шесть месяцев:
# Amazon — 3, Microsoft — 2, Google — 3.

# Условие задачи:
# Дана строка s, состоящая из слов и пробелов. Требуется вернуть длину последнего слова в строке.

# Слово — это максимальная подстрока, состоящая только из символов, не содержащих пробелов.

# Требуемая сложность: 
# O(N), N - длина строки.

# Примеры:
# Ввод: s = "Hello World"
# Вывод: 5
# Объяснение: Последнее слово строки s "World" имеет длину 5.

# Ввод: s = "   fly me   to   the moon  "
# Вывод: 4
# Объяснение: Последнее слово строки s "moon" имеет длину 4.
