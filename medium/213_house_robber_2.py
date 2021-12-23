"""
You are a professional robber planning to rob houses along a street. Each house
has a certain amount of money stashed. All houses at this place are arranged in
a circle. That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected, and it will
automatically contact the police if two adjacent houses were broken into on the
same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the
police.

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
because they are adjacent houses.

Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:

Input: nums = [1,2,3]
Output: 3

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""
from typing import *


class SolutionA:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 4:
            return max(nums)

        rob_so_far_start = [nums[0], max(nums[1], nums[0])]
        for n in range(2, length - 1):
            this_house = nums[n]
            previous = rob_so_far_start[-1]
            odd_previous = rob_so_far_start[-2]
            rob_so_far_start.append(max(previous, this_house + odd_previous))
        max_when_start_robbed = rob_so_far_start[-1]

        rob_so_far_end = [nums[1], max(nums[2], nums[1])]
        for n in range(3, length):
            this_house = nums[n]
            previous = rob_so_far_end[-1]
            odd_previous = rob_so_far_end[-2]
            rob_so_far_end.append(max(previous, this_house + odd_previous))
        max_when_end_robbed = rob_so_far_end[-1]

        return max(max_when_start_robbed, max_when_end_robbed)


class SolutionO1:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 4:
            return max(nums)

        rob_start, not_rob_start = 0, 0
        rob_end, not_rob_end = 0, 0

        for idx, n in enumerate(nums):
            if idx > length - 2:
                # do not take the last part. rob_end will take it
                break
            rob_start, not_rob_start = not_rob_start, max(not_rob_start, rob_start + n)
            rob_end, not_rob_end = not_rob_end, max(
                not_rob_end, rob_end + nums[idx + 1]
            )
            print(not_rob_end, not_rob_start)
        return max(not_rob_end, not_rob_start)


def check(expected, *args):
    classes = [SolutionA, SolutionO1]
    for Solution in classes:
        print(Solution.__name__, expected)
        result = Solution().rob(*args)
        print(result, result == expected)


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    expect = 4
    check(expect, nums)

    nums = [2, 3, 2]
    expect = 3
    check(expect, nums)

    nums = [1, 2, 3]
    expect = 3
    check(expect, nums)

    nums = [1, 1, 1, 2]
    expect = 3
    check(expect, nums)

    nums = [200, 3, 140, 20, 10]
    expect = 340
    check(expect, nums)
