#!/usr/bin/env python

# Mikhail Kolodin
# lc-uni2lists.py 2023-07-09 2023-07-09 1.0

class Node():

    def __init__(self, val: int=0) -> None:
        self.val = val
        self.link = None

class LList():

    def __init__(self, data: list[int]) -> None:
        self.head = None
        if data:
            da = data.copy()
            while da:
                nn = Node(da.pop())
                nn.link = self.head
                self.head = nn

    def line(self) -> list[int]:
        outl = []
        ptr = self.head
        while ptr:
            outl.append(ptr.val)
            ptr = ptr.link
        return outl

def solve(list1: LList, list2: LList) -> LList:
    """solve the problem"""
    
    list3 = LList([])

    ptr1 = list1.head
    ptr2 = list2.head

    lor = []

    while ptr1 and ptr2:
        if ptr1.val <= ptr2.val:
            lor.append(ptr1.val)
            ptr1 = ptr1.link
        else:
            lor.append(ptr2.val)
            ptr2 = ptr2.link

    while ptr1:
        lor.append(ptr1.val)
        ptr1 = ptr1.link

    while ptr2:
        lor.append(ptr2.val)
        ptr2 = ptr2.link

    return LList(lor)


def test(list1: list[int], list2: list[int]) -> list[int]:
    """run 1 test"""

    l1 = LList(list1)
    l2 = LList(list2)

    list3 = solve(l1, l2).line()
    print(f"{list1=}, {list2=} => {list3=}")

test([1, 2, 4], [1, 3, 4])
test([], [])
test([], [0])
     
# list1=[1, 2, 4], list2=[1, 3, 4] => list3=[1, 1, 2, 3, 4, 4]
# list1=[], list2=[] => list3=[]
# list1=[], list2=[0] => list3=[0]

# Объединить два отсортированных списка
#  (https://leetcode.com/problems/merge-two-sorted-lists/)
# Вам даны head’ы двух отсортированных связанных списков list1 и list2. Объедините два списка в один отсортированный список. Список должен быть составлен путем соединения узлов первых двух списков. Верните head объединенного связанного списка.

# Пример 1 (на картинке):
# Ввод: list1 = [1,2,4], list2 = [1,3,4]
# Вывод: [1,1,2,3,4,4]

# Пример 2:
# Ввод: list1 = [], list2 = []
# Вывод: []

# Пример 3:
# Ввод: list1 = [], list2 = [0]
# Вывод: [0]

# есть несоответствие условия и примера: 
# сказано вернуть head, 
# а показано, что возвращается простой список.
# решено добавлением функции line, превращающей связанный список в простой
