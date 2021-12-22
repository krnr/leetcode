"""
Given an array nums with n objects colored red, white, or blue, sort them
in-place so that objects of the same color are adjacent, with the colors in the
order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and
blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""
from typing import *


class SolutionA:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        reds = 0
        whites = 0
        blues = 0
        for n in nums:
            if n == 0:
                reds += 1
            if n == 1:
                whites += 1
            if n == 2:
                blues += 1

        i = 0
        while reds:
            nums[i] = 0
            reds -= 1
            i += 1
        while whites:
            nums[i] = 1
            whites -= 1
            i += 1
        while blues:
            nums[i] = 2
            blues -= 1
            i += 1


class SolutionB:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        If the white pointer is red (nums[white] == 0), we swap with the red
        pointer and move both white and red pointer forward. If the pointer is
        white (nums[white] == 1), the element is already in correct place, so
        we don't have to swap, just move the white pointer forward. If the
        white pointer is blue, we swap with the latest unclassified element.
        """
        red, white, blue = 0, 0, len(nums) - 1
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
