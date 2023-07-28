#!/usr/bin/env python
# Mikhail Kolodin
# lc-delellinked.py 2023-07-28 2023-07-28 1.0

class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LList:
    def __init__(self):
        self.next = None

    def add(self, arr):
        carr = arr.copy()
        while carr:
            self.next = ListNode(carr.pop(), self.next)
            
    def print(self):
        ptr = self.next
        print("[", end="")
        while ptr:
            print(ptr.val, end=", ")
            ptr = ptr.next
        print("]")

    def array(self):
        ptr = self.next
        arr = []
        while ptr:
            arr.append(ptr.val)
            ptr = ptr.next
        return arr


def solve(head, val):
    """solve 1 task"""

    ll = LList()
    ll.add(head)
    # ll.print()

    ptr = ll.next
    while ptr:
        if ptr.next and ptr.next.val == val:
            ptr.next = ptr.next.next
        else:
            ptr = ptr.next

    # ll.print()
    return ll.array()
    

def test(head, val):
    """print 1 test"""
    print(f"{head=}, {val=} => {solve(head, val)}")

test(head = [1,2,6,3,4,5,6], val = 6)
test(head = [], val = 1)


# Удаление элементов из связного списка (https://leetcode.com/problems/remove-linked-list-elements/)

# Сложность: Лёгкая (203)

# Условие задачи: дан указетель на связный список и целое число (val). Надо извлечь из сипска все узлыва, значение в которых равняется val. 

# Итогом должен быть возврат на начало изменненного списка (все опреции будут производиться непосредственно с самим списком). 

# Пример:

# Ввод: head = [1,2,6,3,4,5,6], val = 6
# Вывод: [1,2,3,4,5]

# Ввод: head = [], val = 1
# Вывод: []

# Уточнение: судя по примеру, надо не _извлечь_, а _удалить_ элементы.
