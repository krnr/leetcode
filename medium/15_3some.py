"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:

Input: nums = []
Output: []

Example 3:

Input: nums = [0]
Output: []

Constraints:

0 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
"""
from typing import *
import itertools as it


class SolutionA:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        length = len(nums)
        # for 3 nums we should always have 2 spots left
        for idx in range(length - 2):
            current = nums[idx]
            if current > 0:
                break  # positive sums will never = 0
            if idx > 0 and current == nums[idx - 1]:  # don't run for the same int
                continue
            left, rght = idx + 1, length - 1
            while left < rght:
                three_sum = current + nums[left] + nums[rght]
                if three_sum > 0:
                    rght -= 1
                if three_sum < 0:
                    left += 1
                if three_sum == 0:
                    result.append([current, nums[left], nums[rght]])
                    # avoid duplication
                    while nums[left] == nums[left + 1]:
                        left += 1
                    while nums[rght] == nums[rght - 1]:
                        rght -= 1
                    left += 1
                    rght -= 1
        return result


class SolutionB:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        negatives, positives, zeros = [], [], []
        for n in nums:
            if n == 0:
                zeros.append(n)
            if n < 0:
                negatives.append(n)
            if n > 0:
                positives.append(n)

        N = set(negatives)
        P = set(positives)

        if len(zeros) >= 3:
            result.append((0, 0, 0))
        if zeros:
            for number in P:
                if -number in N:
                    result.add((-number, 0, number))
        # now, when simple cases are over, for each pair of negatives
        # let's check a counterpart in positives
        for x, y in it.combinations(negatives, 2):
            to_check = -1 * (x + y)
            if to_check in positives:
                result.add(tuple(sorted([x, y, to_check])))
        for x, y in it.combinations(positives, 2):
            to_check = -1 * (x + y)
            if to_check in negatives:
                result.add(tuple(sorted([x, y, to_check])))

        return [list(s) for s in result]


def check(expected, *args):
    classes = [SolutionA, SolutionB]
    for Solution in classes:
        print(Solution.__name__, expected)
        result = Solution().threeSum(*args)
        print(result)


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    expect = [[-1, -1, 2], [-1, 0, 1]]
    check(expect, nums)

    nums = []
    expect = []
    check(expect, nums)

    nums = [0]
    expect = []
    check(expect, nums)

    nums = [-2, 0, 0, 2, 2]
    expect = [[-2, 0, 2]]
    check(expect, nums)
