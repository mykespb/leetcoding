#!/usr/bin/env python
# Mikhail Kolodin
# lc-longpalin.py 2023-08-02 2023-09-02 1.0

def solve(s):
    """solve complete task"""
    if len(s) == 0: return ""

    for tlen in range(len(s), 0, -1):
        if sol := solved(s, tlen):
            return sol
        
    return ""


def solved(s, tlen):
    """solve subtask for substring of length tlen"""
    if len(s) == 0: return ""

    for pos in range(len(s) - tlen + 1):
        if good := ispalin(s[pos : pos+tlen]):
            return good

    return ""


def ispalin(s):
    """check por polindromity"""
    return s if s == s[::-1] else False


def test(s):
    """run 1 test"""
    print(f"task: {s=} => {solve(s)}")

test("babad")
test("cbbd")
test("a")

# Given a string s, return the longest palindrome substring in s
