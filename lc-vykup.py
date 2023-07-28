#!/usr/bin/env python
# Mikhail Kolodin
# lc-vykup.py 2023-07-28 2023-07-28 1.0

def solve(ransomNote: str, magazine: str) -> bool:
    """solve 1 task"""
    aRan = list(ransomNote)
    aMag = list(magazine)

    for r in aRan:
        if r in aMag:
            aMag.remove(r)
        else:
            return False
        
    return True


def test(ransomNote, magazine) -> None:
    """print 1 test"""
    print(f"{ransomNote=}, {magazine=} => {solve(ransomNote, magazine)}")

test(ransomNote = "a", magazine = "b")
test(ransomNote = "aa", magazine = "ab")
test(ransomNote = "aa", magazine = "aab")

# ransomNote='a', magazine='b' => False
# ransomNote='aa', magazine='ab' => False
# ransomNote='aa', magazine='aab' => True


# Записка о выкупе (https://leetcode.com/problems/ransom-note/)

# Сложность: Лёгкая 

# Условие задачи: дано две строки:  ransomNote и magazine. Требуется осуществить проверку, может ли строка ransomNote быть получена путем использования букв из строки magazine. 

# Одна буква из magazine может быть исопльзована единажды в ransomNote.

# Пример:

# Ввод: ransomNote = "a", magazine = "b"
# Вывод: false

# Ввод: ransomNote = "aa", magazine = "ab"
# Вывод: false

# Ввод: ransomNote = "aa", magazine = "aab"
# Вывод: true
