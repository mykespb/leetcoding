#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2023
# 2023-03-02 2023-03-02 1.0

# Здесь упрощённая задача: берём просто список, обрабатываем как просят без ограничений.
# Исходный список тоже печатается

from collections import Counter

def proc(arr: list[int]) -> list[int]:
    """обработка"""

    cnt = Counter(arr)
    good = [k for k, v in cnt.items() if v==1 ]
    return sorted(good)

# testing

head = [1,2,3,3,4,4,5]
print(head, '->', proc(head))

head = [1,1,1,2,3]
print(head, '->', proc(head))

# Извлечение дубликатов из  (https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)отсортированного списка II
#  (https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)
# Сложность: Средняя

# Условие задачи: на вход подается указатель на начало связного списка, необходимо удалить все узлы, имеющие дубликаты, то есть в списке должны остаться лишь уникальные значения, которые были в изначальном списке. Необходимо вернуть связный список в отсортированном порядке как и был.

# Пример:

# Ввод: head = [1,2,3,3,4,4,5]
# Вывод: [1,2,5]

# Ввод: head = [1,1,1,2,3]
# Вывод: [2,3]
