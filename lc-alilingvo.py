#!/usr/bin/env python
# Mikhail Kolodin, 2023
# 2023-02-04 2023-02-04 0.1

def fk(k):
    if k in order:
        return order.index(k)
    else:
        return 999

words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"

print(words, order, "->",
    words == sorted(words, key=fk))

words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"

print(words, order, "->",
    words == sorted(words, key=fk))

# ~ Чужой язык

 # ~ (https://leetcode.com/problems/verifying-an-alien-dictionary/)Сложность: Лёгкая

# ~ Условие задачи: на чужом языке они также используют английские строчные буквы, но, возможно, в другом порядке. Порядок алфавита - это некоторая перестановка строчных букв.

# ~ Учитывая последовательность слов, написанных на чужом языке, и порядок алфавита, верните значение true тогда и только тогда, когда данные слова отсортированы лексикографически на этом чужом языке.

# ~ Пример:

# ~ Ввод:  words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# ~ Вывод: true
# ~ Объяснение:

# ~ Ввод: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# ~ Вывод: false
