"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More
formally, if you are on index i on the current row, you may move to either
index i or index i + 1 on the next row.

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:

Input: triangle = [[-10]]
Output: -10
"""
from typing import *


class Solution:
    """Bottom-up"""
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        previous = [n for n in triangle[-1]]
        length = len(triangle)
        n = -2
        while n >= length * -1:
            cur_nums = triangle[n]
            for i, num in enumerate(cur_nums):
                previous[i] = min(previous[i], previous[i+1]) + num
            n -=1
        return previous[0]
