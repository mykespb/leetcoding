#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2023-02-24 2023-02-24 1.0

# Поиск мажоритарного элемента

from collections import Counter as Cnt

def find(arr: list[int]) -> int:
    """найти мажоритарный элемент"""

    return Cnt(arr).most_common(1)[0][0]

nums = [4,2,4]
print(nums, '->', find(nums))

nums = [8, 8, 6, 6, 6, 8, 8]
print(nums, '->', find(nums))

# Условие задачи:
# Дан массив nums размера n. Требуется вернуть мажоритарный элемент.

# Мажоритарный элемент - это элемент, который появляется более n / 2 раз. Вы можете быть уверены, что мажоритарный элемент всегда существует в массиве.

# Примеры:
# Ввод: nums = [4,2,4]
# Вывод: 4

# Ввод: nums = [8, 8, 6, 6, 6, 8, 8]
# Вывод: 8

# [4, 2, 4] -> 4
# [8, 8, 6, 6, 6, 8, 8] -> 8
