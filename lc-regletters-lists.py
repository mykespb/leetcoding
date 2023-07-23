#!/usr/bin/env python

# Mikhail Kolodin
# lc-regletters-lists.py 2023-07-23 2023-07-23 1.0

from string import ascii_letters as letters

def solve(s: str) -> list[str]:
    """solve it"""

    slen = len(s)
    if slen == 0:
        return []
    
    todo = [s]

    for num in range(slen):
        todo = proc(num, todo)

    return todo


def proc(num: int, todo: list[str]) -> list[str]:
    """process next char"""

    next = []
    for elem in todo:
        curr = elem[num]
        if curr in letters:
            left = elem[:num]
            right = elem[num+1:]
            next.append(left + curr.lower() + right)
            next.append(left + curr.upper() + right)
        else:
            next.append(elem)

    return next


def test(s: str) -> None:
    """run a test"""

    print(f"{s=} => {solve(s)}")

test("3z4")
test("a1b2")

# s='3z4' => ['3z4', '3Z4']
# s='a1b2' => ['a1b2', 'a1B2', 'A1b2', 'A1B2']

# task 784, ver.2, with trees

# Перебор регистра букв (https://leetcode.com/problems/letter-case-permutation/)
# Сложность: Средняя
# Условие задачи: на вход подается строка. Надо вывести все комбинации, которые можно составить из данных символов в верхнем и нижнем регистрах. 
# Пример:

# Ввод: s = "a1b2"
# Вывод: ["a1b2","a1B2","A1b2","A1B2"]
# Объяснение:

# Ввод: s = "3z4"
# Вывод: ["3z4","3Z4"]
