#!/usr/bin/env python
# Mikhail Kolodin
# lc-minsumindex.py 2023-08-21 2023-08-21 1.0


def solve(list1: list[str], list2: list[str]) -> list[str]:
    """solve complete task"""
    
    minindex = None
    bestwords = []

    for i1, w1 in enumerate(list1):
        if w1 in list2:
            sumind = i1 + list2.index(w1)
            if minindex is None or sumind < minindex:
                minindex = sumind
                bestwords = [w1]
            elif sumind == minindex:
                bestwords.append(w1)

    return bestwords

    
def test(list1: list[str], list2: list[str]) -> None:
    """run 1 test"""

    print(f"\n{list1=}\n{list2=}\nResult: {solve(list1, list2)}")    

test(list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"])

# list1=['Shogun', 'Tapioca Express', 'Burger King', 'KFC']
# list2=['Piatti', 'The Grill at Torrey Pines', 'Hungry Hunter Steakhouse', 'Shogun']
# Result: ['Shogun']


# Сложность: Лёгкая 

# Условие задачи: дается два массива строк list1 и list2, найдите общие строки с наименьшей суммой индексов.

# Общая строка - это строка, которая появилась как в list1, так и в list2.

# Общая строка с наименьшей суммой индексов - это общая строка, такая, что если она появилась в list1[i] и list2[j], то i + j должно быть минимальным значением среди всех других общих строк.

# Возвращает все общие строки с наименьшей суммой индексов. Верните ответ в любом порядке.

# Пример:

# Ввод: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# Вывод: ["Shogun"]
