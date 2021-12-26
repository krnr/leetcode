"""
Given an array of integers nums and an integer k, return the total number of
continuous subarrays whose sum equals to k.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2

Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

Constraints:

1 <= nums.length <= 2 * 10^4
-1000 <= nums[i] <= 1000
-10^7 <= k <= 10^7
"""
import itertools as it
from collections import defaultdict
from typing import *


class SolutionA:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarrays = 0
        running_sum = 0
        running_sums = defaultdict(int)
        running_sums[0] += 1

        for n in nums:
            running_sum += n
            look_for = running_sum - k
            subarrays += running_sums.get(look_for, 0)
            # if current sum == k, than we will look for 0
            running_sums[running_sum] += 1  # how many arrays with this sum
        return subarrays


class SolutionB:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarrays = 0
        hashmap = defaultdict(int)
        hashmap[0] = 1
        for running in it.accumulate(nums):
            look_for = running - k
            subarrays += hashmap[look_for]
            hashmap[running] += 1
        return subarrays


def check(expected, *args):
    classes = [SolutionA, SolutionB]
    for Solution in classes:
        print(Solution.__name__, *args)
        result = Solution().subarraySum(*args)
        print(result, result == expected)


if __name__ == "__main__":
    nums = [1, 1, 1]
    k = 2
    expect = 2
    check(expect, nums, k)

    nums = [1, 2, 3]
    k = 3
    expect = 2
    check(expect, nums, k)

    nums = [1]
    k = 0
    expect = 0
    check(expect, nums, k)

    nums = [-1, -1, 1]
    k = 0
    expect = 1
    check(expect, nums, k)
