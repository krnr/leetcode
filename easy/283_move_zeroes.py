"""
Given an integer array nums, move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]
 
Constraints:

1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1
 
Follow up: Could you minimize the total number of operations done?
"""
from typing import *


class SolutionA:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        non_zero_ptr = None
        zero_ptr = None
        for i in range(length):
            current = nums[i]
            if not current and zero_ptr is None:
                zero_ptr = i
            if current:
                non_zero_ptr = i
            if zero_ptr is not None and non_zero_ptr is not None:
                nums[zero_ptr], nums[non_zero_ptr] = nums[non_zero_ptr], nums[zero_ptr]
                zero_ptr += 1
                non_zero_ptr = None


class SolutionB:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_zero_ptr = 0
        for i in range(len(nums)):
            if nums[i] and nums[last_zero_ptr] == 0:
                nums[i], nums[last_zero_ptr] = nums[last_zero_ptr], nums[i]
            if nums[last_zero_ptr]:
                last_zero_ptr += 1


def check(expected, nums):
    classes = [SolutionA, SolutionB]
    for Solution in classes:
        n = list(nums)
        print(Solution.__name__, expected)
        Solution().moveZeroes(n)
        print(n, n == expected)


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    expect = [1, 3, 12, 0, 0]
    check(expect, nums)

    nums = [0]
    expect = [0]
    check(expect, nums)

    nums = [0, 1]
    expect = [1, 0]
    check(expect, nums)
