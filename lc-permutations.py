#!/usr/bin/env python
# Mikhail Kolodin
# lc-permutations.py 2023-08-02 2023-09-02 1.0

def solve(nums):

    if nums == []: return []
    if len(nums) == 1: return [nums]

    this = nums[0]
    rest = solve(nums[1:])
    res = []

    for one in rest:
        for pos in range(len(one) + 1):
            res.append( one[:pos] + [this] + one[pos:] )

    return res


def test(nums):
    """run 1 test"""
    print(f"task: {nums=} => {solve(nums)}")

test([11, 22, 33])
test([1, 2, 3])
test([0, 1])
test([1])

# Given an array of distinct integers, return all possible permutations
# (in ay order).
# There is itertools.permutations :)
