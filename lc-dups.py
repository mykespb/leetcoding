#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# lc-dups.py
# Mikhail Kolodin, 2023-04-14
# OK

def qdup(arr: list[int], dist: int) -> bool:
    """
    содержание дубликатов
    """

    for i in range(len(arr) -1):
        for j in range(i+1, len(arr)):
            if i + dist == j and arr[i] == arr[j]:
                return True
            
    return False

# tests

print(qdup([1, 2, 3, 1], 3))
      
print(qdup([1, 0,1, 1], 1))
    
# True
# True

# Содержание дубликатов II

#  (https://leetcode.com/problems/contains-duplicate-ii/)Сложность: Лёгкая

# Условие задачи: дается массив из целых чисел и число k. Необходимо вернуть true, если существуют два уникальных индекса, которые удовлетворяют условиям:

# - nums[i] == nums[j];
# - abs(i - j) <= k.

# Пример:

# Ввод: nums = [1,2,3,1], k = 3
# Вывод: true

# Ввод: nums = [1,0,1,1], k = 1
# Вывод: true
