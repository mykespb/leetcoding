#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2023
# lc-larsubstring-1624.py 2023-12-31 2023-12-31 1.0
# https://leetcode.com/problems/largest-substring-between-two-equal-characters/?envType=daily-question&envId=2023-12-31

def solve(s: str) -> int:
    """solve 1 task"""

    lens = len(s)

    if lens == 0:
        return -1
    
    if lens == 2:
        if s[0] == s[1]:
            return 0
        else:
            return -1

    most = -1

    for pl in range(lens-2):
        cl = s[pl]

        for pr in range(lens-1, pl, -1):
            cr = s[pr]

            if cl == cr:
                most = max(most, pr - pl - 1)

    return most



def test(s: str) -> None: 
    """ show """
    
    print(f"{s=} -> {solve(s)}")


test("")
test("6")
test("aa")
test("abca")
test("cbzxy")
s='' -> -1
s='6' -> -1
s='aa' -> 0
s='abca' -> 2
s='cbzxy' -> -1

# 1624. Largest Substring Between Two Equal Characters
# Easy

# Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.
# A substring is a contiguous sequence of characters within a string.

# Example 1:

# Input: s = "aa"
# Output: 0
# Explanation: The optimal substring here is an empty substring between the two 'a's.
# Example 2:

# Input: s = "abca"
# Output: 2
# Explanation: The optimal substring here is "bc".
# Example 3:

# Input: s = "cbzxy"
# Output: -1
# Explanation: There are no characters that appear twice in s.
 
# Constraints:

# 1 <= s.length <= 300
# s contains only lowercase English letters.
