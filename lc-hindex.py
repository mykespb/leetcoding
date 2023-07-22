#!/usr/bin/env python

# Mikhail Kolodin
# lc-hindex.py 2023-07-22 2023-07-22 1.0

def solve(array):
    """solve the problem"""

    for res in range(1, len(array)):
        if not hindex(array, res):
            return res-1


def hindex(array, ind):
    """calc 1 index fit"""

    return sum([ 1 if x>=ind else 0 for x in array]) >= ind


def test(array):
    """run 1 test"""

    print(f"{array=}, h-index={solve(array)}")

test([3,0,6,1,5])
test([1,3,1])

# array=[3, 0, 6, 1, 5], h-index=3
# array=[1, 3, 1], h-index=1

# https://leetcode.com/problems/h-index/description/
# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

# According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

# Example 1:

# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
# Example 2:

# Input: citations = [1,3,1]
# Output: 1
 
#  Constraints:

# n == citations.length
# 1 <= n <= 5000
# 0 <= citations[i] <= 1000
