"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 10^5
s[i] is a printable ascii character.
"""

from typing import *


class SolutionA:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, rght = 0, len(s) - 1
        while left <= rght:
            s[left], s[rght] = s[rght], s[left]
            left += 1
            rght -= 1


def check(expected, s):
    classes = [SolutionA]
    for Solution in classes:
        n = list(s)
        print(Solution.__name__, expected)
        Solution().reverseString(n)
        print(n, n == expected)


if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    expect = ["o", "l", "l", "e", "h"]
    check(expect, s)

    s = ["H", "a", "n", "n", "a", "h"]
    expect = ["h", "a", "n", "n", "a", "H"]
    check(expect, s)
