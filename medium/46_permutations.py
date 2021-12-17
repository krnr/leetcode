"""
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""
import itertools as it
from typing import *


class SolutionA:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(it.permutations(nums, len(nums)))


class SolutionB:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, permut, permutations):
            if not nums:
                permutations.append(permut)
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1 :], permut + [nums[i]], permutations)

        result = []
        dfs(nums, [], result)
        return result


class SolutionC:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def tree(path, used_elements, permutations):
            if len(path) == len(nums):
                permutations.append(path[:])
                return

            for i, num in enumerate(nums):
                if used_elements[i]:
                    continue

                # mark as used, add to permutation
                path.append(num)
                used_elements[i] = True
                tree(path, used_elements, permutations)

                # remove from permutation, let use again
                path.pop()
                used_elements[i] = False

        result = []
        tree([], [False for _ in nums], result)
        return result


def check(expected, *args):
    classes = [SolutionA, SolutionB, SolutionC]
    for Solution in classes:
        print(Solution.__name__, expected)
        result = Solution().permute(*args)
        print(result)


if __name__ == "__main__":
    nums = [1, 2, 3]
    expect = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    check(expect, nums)

    nums = [0, 1]
    expect = [[0, 1], [1, 0]]
    check(expect, nums)

    nums = [1]
    expect = [[1]]
    check(expect, nums)
