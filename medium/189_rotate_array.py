"""
Given an array, rotate the array to the right by k steps, where k is
non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output:       [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output:       [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Constraints:

1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
0 <= k <= 10^5

Follow up:

Try to come up with as many solutions as you can. There are at least three
different ways to solve this problem.  Could you do it in-place with O(1) extra
space?
"""
from typing import *


class SolutionN2:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not k:
            return
        for _ in range(k):
            self.slide(nums)

    def slide(self, nums):
        for j in range(len(nums) - 1, 0, -1):
            nums[j], nums[j - 1] = nums[j - 1], nums[j]


class SolutionN:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not k:
            return
        length = len(nums)
        limit = length - k % length

        for i, new in enumerate(nums[limit:] + nums[:limit]):
            nums[i] = new


class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not k:
            return
        length = len(nums)
        limit = k % length

        def _reverse(left, rght):
            while left < rght:
                nums[left], nums[rght] = nums[rght], nums[left]
                left += 1
                rght -= 1
            print(nums)

        _reverse(0, length - 1)
        _reverse(limit, length - 1)
        _reverse(0, limit - 1)


def check(expected, nums, k):
    classes = [SolutionN2, SolutionN, Solution1]
    for Solution in classes:
        n = list(nums)
        print(Solution.__name__, expected)
        Solution().rotate(n, k)
        print(n, n == expected)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    expect = [5, 6, 7, 1, 2, 3, 4]
    check(expect, nums, k)

    nums = [-1, -100, 3, 99]
    k = 2
    expect = [3, 99, -1, -100]
    check(expect, nums, k)

    nums = [1, 2, 3]
    k = 4
    expect = [3, 1, 2]
    check(expect, nums, k)
    nums = [1, 2]
    k = 5
    expect = [2, 1]
    check(expect, nums, k)
