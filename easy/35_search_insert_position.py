"""
Given a sorted array of distinct integers and a target value, return the
index if the target is found. If not, return the index where it would be if
it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

Example 4:

Input: nums = [1,3,5,6], target = 0
Output: 0

Example 5:

Input: nums = [1], target = 0
Output: 0
 

Constraints:

1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums contains distinct values sorted in ascending order.
-10^4 <= target <= 10^4
"""
from typing import *
import bisect


class SolutionManual:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        # corner cases
        if target > nums[end]:
            return end + 1
        if target < nums[start]:
            return start

        while start < end:
            current_idx = (start + end) // 2
            print(start, current_idx, end)
            current = nums[current_idx]
            if current == target:
                return current_idx

            if target > current:
                start = current_idx + 1
            else:
                end = current_idx = 1
        return end


class SolutionBisect:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return max(bisect.bisect_left(nums, target), 0)


if __name__ == "__main__":
    classes = [SolutionBisect, SolutionManual]
    nums = [1, 3, 5, 6]
    target = 5
    expect = 2
    for Solution in classes:
        print(Solution.__name__, expect)
        solution = Solution().searchInsert(nums, target)
        assert solution == expect, solution

    nums = [1, 3, 5, 6]
    target = 2
    expect = 1
    for Solution in classes:
        print(Solution.__name__, expect)
        solution = Solution().searchInsert(nums, target)
        assert solution == expect, solution

    nums = [1, 3, 5, 6]
    target = 7
    expect = 4
    for Solution in classes:
        print(Solution.__name__, expect)
        solution = Solution().searchInsert(nums, target)
        assert solution == expect, solution

    nums = [1, 3, 5, 6]
    target = 0
    expect = 0
    for Solution in classes:
        print(Solution.__name__, expect)
        solution = Solution().searchInsert(nums, target)
        assert solution == expect, solution

    nums = [1]
    target = 0
    expect = 0
    for Solution in classes:
        print(Solution.__name__, expect)
        solution = Solution().searchInsert(nums, target)
        assert solution == expect, solution
