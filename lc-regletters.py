#!/usr/bin/env python

# Mikhail Kolodin
# lc-regletters.py 2023-05-31 2023-05-31 1.0

from string import ascii_letters as letters

def solve(s: str) -> str:
    """solve all"""

    print(f"string: {s=}, variants are:")

    poss = []
    for p in range(len(s)):
        if s[p] in letters:
            poss.append(p)
    numlet = len(poss)
    allrep = 2**numlet
    # print(f"we have {numlet=} letters in {poss=}, so we count till {allrep}")

    mystr = list(s)

    for num in range(allrep):
        regs = inpos(num, numlet)

        for p in range(numlet):
            mystr[poss[p]] = mystr[poss[p]].upper() if regs[p] else mystr[poss[p]].lower()
        
        sout = "".join(mystr)
        print(sout)


def inpos(n: int, numlet: int) -> list[int]:
    """make array for cases (lower=0, upper=1)"""

    arr = [0 for _ in range(numlet)]
    pos = 0

    while n:
        if n % 2:
            arr[pos] = 1
        n //= 2
        pos += 1

    return arr


solve("a1b2")
solve("3z4")

# string: s='a1b2', variants are:
# a1b2
# A1b2
# a1B2
# A1B2
# string: s='3z4', variants are:
# 3z4
# 3Z4


# Перебор регистра букв 
# (https://leetcode.com/problems/letter-case-permutation/)
# Сложность: Средняя
# Условие задачи: на вход подается строка. Надо вывести все комбинации, которые можно составить из данных символов в верхнем и нижнем регистрах. 
# Пример:

# Ввод: s = "a1b2"
# Вывод: ["a1b2","a1B2","A1b2","A1B2"]
# Объяснение:

# Ввод: s = "3z4"
# Вывод: ["3z4","3Z4"]
