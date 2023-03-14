#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2023
# 2023-03-15 2023-03-15 1.0

def parens(s: str) -> bool:
    """check correctness"""
    last = []
    for c in s:
        if not last:
            last.append([c, 1])
            continue
        if c == last[-1][0]:
            last[-1][1] += 1
            continue
        if c in '([{':
            last.append([c, 1])
            continue
        if c == ')' and last[-1][0] == '(':
            last[-1][1] -= 1
            if last[-1][1] == 0:
                last = last[:-1]
            continue
        if c == ']' and last[-1][0] == '[':
            last[-1][1] -= 1
            if last[-1][1] == 0:
                last = last[:-1]
            continue
        if c == '}' and last[-1][0] == '{':
            last[-1][1] -= 1
            if last[-1][1] == 0:
                last = last[:-1]
            continue
        return False
    return not last


# tests

s = "()"
print(s, '->', parens(s))

s = "()[]{}"
print(s, '->', parens(s))

s = "(]"
print(s, '->', parens(s))

s = "(())"
print(s, '->', parens(s))

s = "([{}])"
print(s, '->', parens(s))

s = "(((((((((((((((())))))))))))))))"
print(s, '->', parens(s))

s = "(((((((((((((((()))))))))))))))"
print(s, '->', parens(s))


# Скобочная пунктуация

#  (https://leetcode.com/problems/valid-parentheses/)Сложность: Лёгкая

# Условие задачи: дана строка, содержащая в себе только символы: '(', ')', '{', '}', '[', ']'. Надо выполнить проверку на то, корректно ли открыты и закрыты все скобки. 

# Пример:

# Ввод: s = "()"
# Вывод: True

# Ввод: s = "()[]{}"
# Вывод: True

# Ввод: s = "(]"
# Вывод: False

# () -> True
# ()[]{} -> True
# (] -> False
# (()) -> True
# ([{}]) -> True
# (((((((((((((((()))))))))))))))) -> True
# (((((((((((((((())))))))))))))) -> False
