"""
You are a professional robber planning to rob houses along a street. Each house
has a certain amount of money stashed, the only constraint stopping you from
robbing each of them is that adjacent houses have security systems connected
and it will automatically contact the police if two adjacent houses were broken
into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the
police.

Example 1:

Input: nums = [1,2,3,1]
Output: 4

Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: nums = [2,7,9,3,1]
Output: 12

Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
"""
from typing import *


class SolutionA:
    def rob(self, nums: List[int]) -> int:
        robbed = []
        for idx, n in enumerate(nums):
            if idx == 0:
                robbed.append(n)
            elif idx == 1:
                robbed.append(max(robbed[0], n))
            else:
                robbed.append(max(robbed[idx - 1], robbed[idx - 2] + n))
            print(robbed)
        return robbed[-1]


def check(expected, *args):
    classes = [SolutionA]
    for Solution in classes:
        print(Solution.__name__, expected)
        result = Solution().rob(*args)
        print(result)


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    expect = 4
    check(expect, nums)

    nums = [2, 7, 9, 3, 1]
    expect = 12
    check(expect, nums)

    nums = [2, 1, 1, 2]
    expect = 4
    check(expect, nums)
