#!/usr/bin/env python
# Mikhail Kolodin
# lc-countingstr.py 2023-08-14 2023-08-14 1.0


def solve(n: int) -> str:
    """solve complete task"""
    
    if n == 1:
        return "1"
    
    kune = str(n)
    for rept in range(1, n):
        seq = makeseq(kune)
        kune = readit(seq)
        # print(f"{rept=}, {seq=}, {kune=}")

    return kune


def makeseq(s: str) -> list[str]:
    out = []
    pred = ""
    elem = ""
    for c in s:
        if c == pred:
            elem += c
        else:
            if elem:
                out.append(elem)
            elem = c
            pred = c
    if elem:
        out.append(elem)

    # print(f"{out=}")
    return out


def readit(los: list[str]) -> str:
    out = ""

    # print(f"{los=}")
    for elem in los:
        out += str(len(elem)) + elem[0]

    return out


def test(n: int) -> None:
    """run 1 test"""
    
    assert n > 0
    print(f"task: {n=} => {solve(n)}")

for i in range(1, 10):
    test(i)

# task: n=1 => 1
# task: n=2 => 12
# task: n=3 => 1113
# task: n=4 => 3114
# task: n=5 => 132115
# task: n=6 => 1113122116
# task: n=7 => 311311222117
# task: n=8 => 13211321322118
# task: n=9 => 1113122113121113222119

# Считалка

#  (https://leetcode.com/problems/count-and-say/)Сложность: Средняя 

# Условие задачи: последовательность "Посчитай и скажи" - это последовательность строк цифр, определяемая рекурсивной формулой:

# посчитайте и скажите(1) = "1"
# countAndSay(n) - это способ, которым вы бы "сказали" строку цифр из countAndSay(n-1), которая затем преобразуется в другую строку цифр.
# Чтобы определить, как вы "произносите" строку цифр, разделите ее на минимальное количество подстрок таким образом, чтобы каждая подстрока содержала ровно одну уникальную цифру. Затем для каждой подстроки произнесите количество цифр, затем произнесите цифру. Наконец, объедините каждую указанную цифру.

# Например, высказывание и преобразование для цифровой строки "3322251" (*во вложении)

# Дается положительное целое число n, верните n-й член последовательности "посчитай и скажи".

# Пример:

# Ввод: n = 1
# Вывод: "1"