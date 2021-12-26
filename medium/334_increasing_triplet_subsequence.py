"""
Given an integer array nums, return true if there exists a triple of indices
(i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such
indices exists, return false.

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

Constraints:

1 <= nums.length <= 5 * 10^5
-2^31 <= nums[i] <= 2^31 - 1

Follow up: Could you implement a solution that runs in O(n) time complexity and
O(1) space complexity?
"""
from typing import *


class SolutionA:
    def increasingTriplet(self, nums: List[int]) -> bool:
        length = len(nums)

        if length < 3:
            return False

        left, midl = nums[0], float('inf')

        for i in range(1, length):
            current = nums[i]
            if current <= left:
                left = current
            elif current <= midl:
                midl = current
            else:
                return True
        return False


def check(expected, n):
    classes = [SolutionA]
    for Solution in classes:
        print(Solution.__name__, expected)
        result = Solution().increasingTriplet(n)
        print(result, result == expected)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    expect = True
    check(expect, nums)

    nums = [5, 1, 6]
    expect = False
    check(expect, nums)

    nums = [5, 4, 3, 2, 1]
    expect = False
    check(expect, nums)

    nums = [2, 1, 5, 0, 4, 6]
    expect = True
    check(expect, nums)
