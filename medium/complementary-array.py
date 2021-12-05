#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
You are given an integer array nums of even length n and an integer limit. In
one move, you can replace any integer from nums with another integer between 1
and limit, inclusive.

The array nums is complementary if for all indices i (0-indexed), nums[i] +
nums[n - 1 - i] equals the same number. For example, the array [1,2,3,4] is
complementary because for all indices i, nums[i] + nums[n - 1 - i] = 5.

Return the minimum number of moves required to make nums complementary.


Example 1:

Input: nums = [1,2,4,3], limit = 4
Output: 1
Explanation: In 1 move, you can change nums to [1,2,2,3] (underlined elements are changed).
nums[0] + nums[3] = 1 + 3 = 4.
nums[1] + nums[2] = 2 + 2 = 4.
nums[2] + nums[1] = 2 + 2 = 4.
nums[3] + nums[0] = 3 + 1 = 4.
Therefore, nums[i] + nums[n-1-i] = 4 for every i, so nums is complementary.

Example 2:

Input: nums = [1,2,2,1], limit = 2
Output: 2
Explanation: In 2 moves, you can change nums to [2,2,2,2]. You cannot change any number to 3 since 3 > limit.

Example 3:

Input: nums = [1,2,1,2], limit = 2
Output: 0
Explanation: nums is already complementary.

https://leetcode.com/problems/minimum-moves-to-make-array-complementary/
"""
from collections import Counter
from typing import *


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        middle = int(len(nums) / 2)
        pairs_sums = [a + b for a, b in zip(nums[:middle], nums[::-1][:middle])]
        print(pairs_sums)
        if is_complimentary(pairs_sums):
            return 0

        cntr = Counter(pairs_sums)
        most_common_sum = cntr.most_common(1)[0][0]
        changes = [0] * middle
        for i, pair in enumerate(pairs_sums):
            left = nums[i]
            right = nums[-i - 1]
            current_sum = left + right
            print("left:", left)
            print("right:", right)
            print("current_sum:", current_sum)
            print("changes:", changes)
            minim = min(left, right)
            maxim = max(left, right)

            if current_sum == pair:
                continue
            elif minim + 1 <= most_common_sum < left + right:
                changes[i] == 1
            elif maxim + limit > most_common_sum > left + right:
                changes[i] == 1
            elif minim + 1 > most_common_sum > left + right:
                changes[i] == 2
            else:
                changes[i] == 2
        return sum(changes)


def is_complimentary(array: List[int]):
    return len(set(array)) == 1


nums = [1, 2, 4, 3]
limit = 4
answer = Solution().minMoves(nums, limit)
assert answer == 1, answer

nums = [1, 2, 2, 1]
limit = 2
answer = Solution().minMoves(nums, limit)
assert answer == 2, answer

nums = [1, 2, 1, 2]
limit = 2
answer = Solution().minMoves(nums, limit)
assert answer == 0, answer
