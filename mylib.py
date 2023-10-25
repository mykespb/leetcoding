#!/usr/bin/env python
# Mikhail Kolodin
# mylib.py 2023-07-28 2023-10-25 1.2

# Классы LinkedList, LinkNode

class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.next = None

    def addList(self, arr):
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

    def __str__(self):
        ptr = self.next
        sout = "["
        while ptr:
            if len(sout) > 1:
                sout += ", "
            sout += str(ptr.val)
            ptr = ptr.next
        sout += "]"
        return sout

    def asList(self):
        ptr = self.next
        arr = []
        while ptr:
            arr.append(ptr.val)
            ptr = ptr.next
        return arr
