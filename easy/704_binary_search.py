"""
Given an array of integers nums which is sorted in ascending order, and an
integer target, write a function to search target in nums. If target exists,
then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 
Constraints:

1 <= nums.length <= 10^4
-10^4 < nums[i], target < 10^4
All the integers in nums are unique.
nums is sorted in ascending order.
"""
from typing import *
import bisect


class SolutionInspect:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1


class SolutionBisect:
    def search(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target) if target in nums else -1


class SolutionManual:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while end >= start:
            mid = (start + end) // 2
            in_middle = nums[mid]
            if target == in_middle:
                return mid
            if target > in_middle:
                start = mid + 1
            else:
                end = mid - 1
        return -1


if __name__ == "__main__":
    classes = [SolutionInspect, SolutionBisect, SolutionManual]
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    expect = 4
    for Solution in classes:
        print(Solution.__name__, expect)
        solution = Solution().search(nums, target)
        assert solution == expect, solution
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    expect = -1
    for Solution in classes:
        print(Solution.__name__, expect)
        solution = Solution().search(nums, target)
        assert solution == expect, solution
