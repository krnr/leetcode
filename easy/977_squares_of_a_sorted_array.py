"""
Given an integer array nums sorted in non-decreasing order, return an array of
the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,11,3]
Output: [4,9,9,49,121]

Constraints:

1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in non-decreasing order.

Follow up: Squaring each element and sorting the new array is very trivial,
could you find an O(n) solution using a different approach?
"""
import collections
from typing import *


class SolutionOn:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        pointer_left, pointer_rght = 0, len(nums) - 1
        result = collections.deque()
        while pointer_rght >= pointer_left:
            value_left = abs(nums[pointer_left])
            value_rght = abs(nums[pointer_rght])
            if value_left > value_rght:
                result.appendleft(value_left ** 2)
                pointer_left += 1
            else:
                result.appendleft(value_rght ** 2)
                pointer_rght -= 1
        return list(result)


class SolutionSimple:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return list(sorted(n * n for n in nums))


def check(expected, *args):
    classes = [SolutionSimple, SolutionOn]
    for Solution in classes:
        print(Solution.__name__, expected)
        solution = Solution().sortedSquares(*args)
        print(solution, solution == expected)


if __name__ == "__main__":
    nums = [-4, -1, 0, 3, 10]
    expect = [0, 1, 9, 16, 100]
    check(expect, nums)

    nums = [-7, -3, 2, 3, 11]
    expect = [4, 9, 9, 49, 121]
    check(expect, nums)
