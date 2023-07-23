#!/usr/bin/env python

# Mikhail Kolodin
# lc-dailytemp.py 2023-07-22 2023-07-22 1.0

def solve(array):
    """solve the problem"""

    res = [ 0 for i in range(len(array)) ]
    for i in range(len(array) - 1):
        for j in range(i+1, len(array)):
            if array[i] < array[j]:
                res[i] = j - i 
                break

    return res

def test(array):
    """run 1 test"""

    print(f"{array=}, result={solve(array)}")

test([73,74,75,71,69,72,76,73])
test([30,40,50,60])
test([30,60,90])

# array=[73, 74, 75, 71, 69, 72, 76, 73], result=[1, 1, 4, 2, 1, 1, 0, 0]
# array=[30, 40, 50, 60], result=[1, 1, 1, 0]
# array=[30, 60, 90], result=[1, 1, 0]

# https://leetcode.com/problems/daily-temperatures/
# 739. Daily Temperatures
# Medium
# 11.2K
# 246
# Companies
# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]

# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100
