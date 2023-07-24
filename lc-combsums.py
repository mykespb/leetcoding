#!/usr/bin/env python
# Mikhail Kolodin
# lc-combsums.py 2023-07-24 2023-07-24 1.0

from itertools import compress

def solve(cand, target):
    arr = list(filter(lambda x: x<=target, cand))
    arr.sort(reverse = True)
    res = set()

    for ind in range(2**len(arr)):
        fil = [ int(x) for x in format(ind, 'b').rjust(len(arr), '0')]
        nums = list(compress(arr, fil))

        if sum(nums) == target:
            nova = tuple(sorted(nums, reverse=True))
            res |= {nova}

    return res


def test(cand, target):
    print(f"\ncombinations={cand}, {target=} => {solve(cand, target)}")

test(cand = [10,1,2,7,6,1,5], target = 8)
test(cand = [2,5,2,1,2], target = 5)

# combinations=[10, 1, 2, 7, 6, 1, 5], target=8 => {(6, 2), (6, 1, 1), (5, 2, 1), (7, 1)}
# combinations=[2, 5, 2, 1, 2], target=5 => {(2, 2, 1), (5,)}

# Комбинация сумм II

#  (https://leetcode.com/problems/combination-sum-ii/)Сложность: Средняя 

# Условие задачи: на вход дается список возможных кандидатов и целевое значение суммы, необходимо вывести все комбинации, которыми можно получить целевое значение. 

# Каждое число из списка кандидатов должно содержаться в конечном подсписке из ответов ровно один раз.

# Результирующий ответ не должен содержать в себе дубликатов. 

# Пример:

# Ввод: candidates = [10,1,2,7,6,1,5], target = 8
# Вывод: [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]

# Ввод:  candidates = [2,5,2,1,2], target = 5
# Вывод: [
# [1,2,2],
# [5]
# ]

# Решение задачи (https://telegra.ph/Kombinaciya-summ-II-Reshenie-zadachi-11-03)

# Примечание: метод неэффективный, выполняет почти полный перебор.
# Надо бы идти по всему вниз упоорядоченному списку кандидатов, пока не будет превышение суммы target.
# Для этого потом будет представлено другое решение, 
# здесь хотел поработать с двоичным разложением для выбора кандидатов.
