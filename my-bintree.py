#!/usr/bin/env python
# Mikhail Kolodin
# my-bintree.py 2023-10-25 2023-10-25 1.0

# Классы BinTree, BinTreePtr

from math import log2


# ---------------------------------------------------------------------------

class BinTree:
    """Binary Tree"""

    def __init__(self, data: list[int] = None):
        """make init"""

        assert type(data) == list

        if data:
            self.data = data.copy()
            self.length = len(self.data)
            self.levels = int(log2(self.length)) + 1
            self.size = 2 ** self.levels - 1
        else:
            self.data = []
            self.length = 0
            self.levels = 0
            self.size = 0


    def is_empty(self):
        """checks if tree is empty"""

        return self.length == 0


    def has_elements(self, howmany=1):
        """checks if BinTreePtr has at least 'howmany' elements"""

        return self.length >= howmany


    def get_value(self, ptr):
        """return requested value at node ptr"""
        
        if self.has_elements(ptr-1):
            return self.data[ptr]
        else:
            return None


    def set_value(self, ptr=0, value=0):
        """set new value to node ptr, and returns it"""

        if self.has_elements(ptr-1):
            self.data[ptr] = value
            return self.data[ptr]
        else:
            return None


    # def lengthen(self):
    #     """make it max length in size, filling tail with Nones, correcting other vars"""
    #     ...
        

    # def shorten(self):
    #     """shorten it, deleting tailing Nones, correcting other vars"""
    #     ...
        

    # def rebalance(self):
    #     """make this tree well-balanced"""
    #     ...
        

    # def __str__(self):
    #     """print it"""
    #     ...


    # def __repr__(self):
    #     """represent it"""
    #     ...

# ---------------------------------------------------------------------------

class BinTreePtr:
    """pointer to some place in external BinTree"""

    def __init__(self, root: BinTree):
        """make init"""

        assert type(root) == BinTree

        self._ptr = 0 if len(root.data) else None
        self._root = root


    def go_up(self):
        """move ptr to upper node"""

        if self._ptr is not None:
            self._ptr //= 2


    def go_left(self):
        """go sub-left, if possible"""
        
        if self.has_left():
            self._ptr = self._ptr * 2 + 1


    def go_right(self):
        """go sub-right, if possible"""
        
        if self.has_right():
            self._ptr = self._ptr * 2 + 2


    def has_left(self):
        """check if left child exists"""
        
        tobe = self._ptr * 2 + 1
        return self.exists(tobe)


    def has_right(self):
        """check if right child exists"""
    
        tobe = self._ptr * 2 + 2
        return self.exists(tobe)


    def del_left(self):
        """deletes left subtree at ptr and stays at place, recalc all metrics of BinTree"""
        ...


    def del_right(self):
        """deletes right subtree at ptr and stays at place, recalc all metrics of BinTree"""
        ...


    def del_node(self):
        """deletes node at ptr and moves up, if possible, recalc all metrics of BinTree"""
        ...


    def add_left(self, value):
        """if is_leaf, adds left sibling, else noop, recalc all metrics of BinTree"""
        ...


    def add_right(self, value):
        """if is_leaf, adds right sibling, else noop, recalc all metrics of BinTree"""
        ...


    def is_empty(self):
        """checks if BinTreePtr is empty, same as BinTree.is_empty()"""

        return self._root.length == 0


    def has_elements(self):
        """checks if BinTreePtr is not empty same as BinTree.has_elements()"""

        return self._root.length != 0


    def is_leaf(self):
        """check if we are at final leaf"""
        
        return not self.is_node()


    def is_node(self):
        """check if we are at non-final node"""
        
        return self.has_left() or self.has_right()


    def is_root(self):
        """check if we are at root = tree top"""

        if self._ptr is not None:
            return self._ptr == 0
        else:
            return False


    def exists(self, num):
        """check if requested node exists in tree"""
        
        return self._root.size > num and self._root.data[num] is not None


    def get_value(self):
        """return requested value"""
        
        if self._ptr is not None:
            return self._root.data[self._ptr]
        else:
            return None


    @property
    def ptr(self):
        """return current index"""
        
        return self._ptr


    def get_value(self):
        """return requested value"""
        
        return self._root.data[self._ptr]


    def set_value(self, value):
        """set new value to current node and return it"""

        self._root.data[self._ptr] = value
        return value


    # def __str__(self):
    #     """print sub-tree"""
    #     ...


    # def __repr__(self):
    #     """represent sub-tree"""
    #     ...


    # def rotate_left(self):
    #     """make left rotation of tree relatively to current node"""
    #     ...


    # def rotate_roght(self):
    #     """make right rotation of tree relatively to current node"""
    #     ...

    # ---------------------------------------------------------------------------

