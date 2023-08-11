#!/usr/bin/env python
# Mikhail Kolodin
# lc-alien.py 2023-08-11 2023-08-11 1.0


def solve(words: list[str], order: str) -> bool:
    """solve complete task"""
    
    return words == sorted(words, key = lambda c: order.index(c) if c in order else 99999999)


def test(words: list[str], order: str) -> None:
    """run 1 test"""
    print(f"task: {words=}, {order=} => {solve(words, order)}")


test(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz")
test(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz")

# task: words=['hello', 'leetcode'], order='hlabcdefgijkmnopqrstuvwxyz' => True
# task: words=['word', 'world', 'row'], order='worldabcefghijkmnpqstuvxyz' => False

# Чужой язык

#  (https://leetcode.com/problems/verifying-an-alien-dictionary/)Сложность: Лёгкая

# Условие задачи: на чужом языке они также используют английские строчные буквы, но, возможно, в другом порядке. Порядок алфавита - это некоторая перестановка строчных букв.

# Учитывая последовательность слов, написанных на чужом языке, и порядок алфавита, верните значение true тогда и только тогда, когда данные слова отсортированы лексикографически на этом чужом языке.

# Пример:

# Ввод:  words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Вывод: true
# Объяснение:

# Ввод: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Вывод: false
