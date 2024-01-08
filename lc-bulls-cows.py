#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2023
# lc-bulls-cows.py 2024-01-07 2024-01-08 1.1

def solve(secret: str, guess: str) -> int:
    """solve 1 task"""

    LEN = 4     # length of both strings

    a, b = list(secret), list(guess)
    assert len(a) == LEN
    assert len(b) == LEN

    bulls = cows = 0 

    for i in range(LEN):
        if a[i] == b[i]:
            bulls += 1
            a[i] = b[i] = '.'

    for i in range(LEN):
        for j in range(LEN):
            if i == j or a[i] == '.' or b[j] == '.':
                continue
            if a[i] == b[j]:
                cows += 1
                a[i] = b[j] = '.'

    return f"{bulls}A{cows}B"


def test(secret: str, guess: str) -> None: 
    """ show """
    
    print(f"{secret=}, {guess=} -> {solve(secret, guess)}")


test(secret = "1807", guess = "7810")
test(secret = "1123", guess = "0111")

# secret='1807', guess='7810' -> 1A3B
# secret='1123', guess='0111' -> 1A1B


# Быки и коровы 
# (https://leetcode.com/problems/bulls-and-cows/)

# Сложность: Средняя

# Условие задачи: разыгрывается партия, в которой мы просим оппонента угадать число. После первой попытки мы мы говорим другу количество отданных цифр и неотгаданных. 

# Быки - правильные цифры, находящиеся на нужных позициях. 

# Коровы - правильные числа, но находящиеся на соответствующих позициях.

# Задача - выдать подсказку в формате "xAyB", где x - количество быков, y - количество коров. 

# Пример:

# Ввод: secret = "1807", guess = "7810"
# Вывод: "1A3B"
# Объяснение:

# Ввод: secret = "1123", guess = "0111"
# Вывод: "1A1B"

# Решение задачи (https://telegra.ph/Byki-i-korovy-Reshenie-zadachi-09-02)
