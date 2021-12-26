"""
Given an integer array nums, return an array answer such that answer[i] is
equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the
division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity?
(The output array does not count as extra space for space complexity analysis.)
"""
from typing import *


class SolutionA:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1 for _ in nums]
        left, rght = 1, 1

        for i in range(len(nums)):
            products[i] *= left
            products[~i] *= rght
            left *= nums[i]
            rght *= nums[~i]
        return products


def check(expected, *args):
    classes = [SolutionA]
    for Solution in classes:
        print(Solution.__name__, *args)
        result = Solution().productExceptSelf(*args)
        print(result, result == expected)


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    expect = [24, 12, 8, 6]
    check(expect, nums)

    nums = [-1, 1, 0, -3, 3]
    expect = [0, 0, 9, 0, 0]
    check(expect, nums)
