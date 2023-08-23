#!/usr/bin/env python
# Mikhail Kolodin
# lc-oneedit.py 2023-08-23 2023-08-23 1.0

def solve(s: str, t: str) -> bool:
    """solve complete task"""

    return try_insert(s, t) or try_delete(s, t) or try_change(s, t)
    

def try_insert(s: str, t: str) -> bool:
    """solve insertion subtask"""

    chars = set(t)

    for pos in range(0, len(s)+1):
        for char in chars:
            nova = s[:pos] + char + s[pos:]
            if nova == t:
                return True

    return False


def try_delete(s: str, t: str) -> bool:
    """solve deletion subtask"""

    for pos in range(len(s)):
        nova = s[:pos] + s[pos+1:]
        if nova == t:
            return True

    return False


def try_change(s: str, t: str) -> bool:
    """solve changing subtask"""

    chars = set(t)

    for pos in range(0, len(s)+1):
        for char in chars:
            nova = s[:pos-1] + char + s[pos:]
            if nova == t:
                return True

    return False


def test(s: str, t: str) -> None:
    """run 1 test"""

    print(f"{s=}, {t=} => {solve(s, t)}")    

test(s = "ab", t = "acb")
test(s = "", t = "")

# s='ab', t='acb' => True
# s='', t='' => False

# Одно редактирование

#  (https://leetcode.com/problems/one-edit-distance/)Сложность задачи: Средняя

# Условие задачи:
# Даны две строки s и t. Требуется вернуть true, если обе они находятся на расстоянии редактирования друг от друга, в противном случае вернуть false.

# Говорят, что строка s находится на расстоянии редактирования от строки t, если вы можете:
#     • Вставить ровно один символ в s, чтобы получить t.
#     • Удалить ровно один символ из s, чтобы получить t.
#     • Заменить ровно один символ s другим символом, чтобы получить t.

# Пример:
# Ввод: s = "ab", t = "acb"
# Вывод: true
# Объяснение: Мы можем вставить 'c' в s, чтобы получить t.

# Ввод: s = "", t = ""
# Вывод: false

# Решение задачи (https://telegra.ph/Reshenie-zadachi-08-08)