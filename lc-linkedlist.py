#!/usr/bin/env python
# Mikhail Kolodin
# lc-linkedlist.py 2023-07-28 2023-07-28 1.0

# Классы LinedList, LinkNode

class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList:
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
