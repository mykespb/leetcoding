#!/usr/bin/env python
# Mikhail Kolodin
# lc-zigzag.py 2023-10-03 2023-10-03 1.0


def solve(s, numRows):
    """solve 1 task"""

    out = ["" for _ in range(numRows)]
    step = 1
    row = 0

    for c in s:
        out[row] += c
        row += step

        if row < 0:
            row = 1
            step = 1
        elif row == numRows:
            row = numRows - 2
            step = -1

    return "" . join(out)


def test(s, numRows):
    """run 1 test"""

    print(f"{s=}, {numRows=} => {solve(s, numRows)}")    

test(s = "PAYPALISHIRING", numRows = 3)
test(s = "PAYPALISHIRING", numRows = 4)

# s='PAYPALISHIRING', numRows=3 => PAHNAPLSIIGYIR
# s='PAYPALISHIRING', numRows=4 => PINALSIGYAHRPI

# Зигзагообразная обработка текста

#  (https://leetcode.com/problems/zigzag-conversion/)
# 
# Сложность: Средняя

# Условие задачи: строка "PAYPALISHIRING" при разбиении на чтение зигзагом имеет следующий вид.
# P      A     H     N
# A  P  L  S  I   I  G
# Y       I      R

# Необходимо, используя данный шаблон и количество рядов для зигзага, преобразовать входную строку к данному выводу. То есть после трансформации получится строка "PAHNAPLSIIGYIR".

# Пример:

# Ввод: s = "PAYPALISHIRING", numRows = 3
# Вывод: "PAHNAPLSIIGYIR"

# Ввод: s = "PAYPALISHIRING", numRows = 4
# Вывод:
# Объяснение: 
# P      I       N
# A   L S    I G
# Y A   H R
# P      I