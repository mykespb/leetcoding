#!/usr/bin/env python
# Mikhail Kolodin
# lc-stringgcd.py 2023-08-13 2023-08-13 1.0


def solve(str1: str, str2: str) -> str:
    """solve complete task"""
    
    if (len1 := len(str1)) == 0 or ((len2 := len(str2)) == 0):
        return ""

    if len1 > len2:
        str1, str2 = str2, str1
        len1, len2 = len2, len1

    for isub in range(len1, 0, -1):
        if isdiv(str1, str1[:isub]) and isdiv(str2, str1[:isub]):
            return str1[:isub]

    return ""


def isdiv(s1: str, s2: str) -> bool:
    """check divisibility"""

    l1, l2 = len(s1), len(s2)
    if l1 % l2:
        return False
    
    for chunk in range(l1 // l2 + 1):
        if s1[chunk * l2 : (chunk+1) * l2] == s2:
            return True
        
    return False


def test(str1: str, str2: str) -> None:
    """run 1 test"""
    
    print(f"task: {str1=}, {str2=} => {solve(str1, str2)}")

test(str1 = "ABCABC", str2 = "ABC")
test(str1 = "ABABAB", str2 = "ABAB")

# task: str1='ABCABC', str2='ABC' => ABC
# task: str1='ABABAB', str2='ABAB' => AB

# Наибольший общий делитель строки 

#  (https://leetcode.com/problems/greatest-common-divisor-of-strings/)
# Сложность: Лёгкая 

# Условие задачи: для двух строк s и t мы говорим "t делит s" тогда и только тогда, когда s = t + ... + t (т.е. t объединяется с самим собой один или несколько раз).

# Дается две строки str1 и str2, верните самую большую строку x, такую, что x делит как str1, так и str2.

# Пример:

# Ввод: str1 = "ABCABC", str2 = "ABC"
# Вывод: "ABC"

# Ввод: str1 = "ABABAB", str2 = "ABAB"
# Вывод: "AB"