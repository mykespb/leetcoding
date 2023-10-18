#!/usr/bin/env python
# Mikhail Kolodin
# lc-colexcel.py 2023-10-18 2023-10-18 1.0

import string

chars = string.ascii_uppercase
alen = len(chars)

print(chars, alen)

def solve(num):
    """solve 1 task"""

    if num < alen:
        return chars[num-1]
    
    num -= alen
    up, low = num // alen, num % alen

    return chars[up] + chars[low-1]


def test(num):
    """run 1 test"""

    print(f"\n{num=} => {solve(num)}")    

test(1)
test(28)
print()


# num=1 => A

# num=28 => AB

# Столбцы таблицы Excel 

# (https://leetcode.com/problems/excel-sheet-column-title/)

# Сложность: Лёгкая 

# Условие задачи: на вход подается номер столбца, необходимо конвертировать его в буквенное представление, которое будет использоваться в таблице-Excel.

# Пример:

# Ввод:columnNumber = 1
# Вывод: "A"

# Ввод: columnNumber = 28
# Вывод: "AB"

# Решение задачи (https://telegra.ph/Stolbcy-tablicy-Excel-Reshenie-zadachi-10-19)
