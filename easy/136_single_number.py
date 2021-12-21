"""
Given a non-empty array of integers nums, every element appears twice except
for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only
constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1

Example 2:

Input: nums = [4,1,2,1,2]
Output: 4

Example 3:

Input: nums = [1]
Output: 1

Constraints:

1 <= nums.length <= 3 * 10^4
-3 * 10^4 <= nums[i] <= 3 * 10^4
Each element in the array appears twice except for one element which appears only once.
"""
from typing import *
from collections import Counter


class SolutionA:
    def singleNumber(self, nums: List[int]) -> int:
        ctr = Counter(nums)
        least = ctr.most_common()[-1]
        return least[0]


class SolutionB:
    def singleNumber(self, nums: List[int]) -> int:
        return sum(set(nums) * 2 - set(nums))


class SolutionC:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res


def check(expected, *args):
    classes = [SolutionA, SolutionB, SolutionC]
    for Solution in classes:
        print(Solution.__name__, expected)
        result = Solution().singleNumber(*args)
        print(result == expected)


if __name__ == "__main__":
    nums = [2, 2, 1]
    expect = 1
    check(expect, nums)

    nums = [4, 1, 2, 1, 2]
    expect = 4
    check(expect, nums)

    nums = [1]
    expect = 1
    check(expect, nums)
