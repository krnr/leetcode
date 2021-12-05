#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
You are given an integer array _nums_ and an integer _k_. You are asked to
distribute this array into k subsets of equal size such that there are no two
equal elements in the same subset.

A subset's incompatibility is the difference between the maximum and minimum
elements in that array.

Return the minimum possible sum of incompatibilities of the k subsets after
distributing the array optimally, or return -1 if it is not possible.

A subset is a group integers that appear in the array with no particular order.

 
Example 1:

Input: nums = [1,2,1,4], k = 2
Output: 4
Explanation: The optimal distribution of subsets is [1,2] and [1,4].
The incompatibility is (2-1) + (4-1) = 4.
Note that [1,1] and [2,4] would result in a smaller sum, but the first subset contains 2 equal elements.

Example 2:

Input: nums = [6,3,8,1,3,1,2,2], k = 4
Output: 6
Explanation: The optimal distribution of subsets is [1,2], [2,3], [6,8], and [1,3].
The incompatibility is (2-1) + (3-2) + (8-6) + (3-1) = 6.
"""
import typing as t
from collections import Counter


class Solution:
    def minimumIncompatibility(self, nums: t.List[int], k: int) -> int:
        nums.sort()
        size = len(nums) / k
        buckets = [[] for _ in range(k)]
        cntr = Counter(nums)

        for n in nums:
            print("num:", n)
            print("buckets:", buckets)
            if cntr[n] > len(buckets):
                return -1

            for b in buckets:
                if n not in b and len(b) < size:
                    b.append(n)
        return sum(max(b) - min(b) for b in buckets)


nums = [1, 2, 1, 4]
k = 2
answer = Solution().minimumIncompatibility(nums, k)
assert answer == 4, answer

nums = [6, 3, 8, 1, 3, 1, 2, 2]
k = 4
answer = Solution().minimumIncompatibility(nums, k)
assert answer == 6, answer

nums = [5, 3, 3, 6, 3, 3]
k = 3
answer = Solution().minimumIncompatibility(nums, k)
assert answer == -1, answer
