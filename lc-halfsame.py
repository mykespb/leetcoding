#!/usr/bin/enc python

# Mikhail Kolodin, 2023-04-20
# halfsame.py 2023-04-20 2023-04-20 1.0

def same(s: str) -> bool:
    """check sameness"""

    vowels = 'aeiouy'

    s = s.lower()
    slenh = len(s) // 2

    s1, s2 = s[:slenh], s[slenh:]

    cnt1 = sum([c in vowels for c in s1])
    cnt2 = sum([c in vowels for c in s2])

    return cnt1 == cnt2

# tests

print(same("book"))
# True
print(same("gammaommuk"))
# True
print(same("bookeyrskp"))
# False


# Проверка схожести половин строки

#  (https://leetcode.com/problems/determine-if-string-halves-are-alike/)Сложность: Лёгкая 

# Условие задачи: на вход подается строка четной длины. Далее проводится разделение на две равные части.

# Две строки называются схожими, если в них находится одно и то же количество гласных вне зависимости от регистра.

# Необходимо проверить схожесть двух строк, полученных разбиением по середине.

# Пример:

# Ввод: s = "book"
# Вывод: true
