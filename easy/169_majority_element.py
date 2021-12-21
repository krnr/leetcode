"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You
may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:

n == nums.length
1 <= n <= 5 * 10^4
-2^31 <= nums[i] <= 2^31 - 1

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
from collections import Counter
from typing import *


class SolutionA:
    def majorityElement(self, nums: List[int]) -> int:
        ctr = Counter(nums)
        return ctr.most_common(n=1)[0][0]


class SolutionB:
    def majorityElement(self, nums: List[int]) -> int:
        # We first assume that our first num is the majority element
        count = 1
        result = nums[0]

        for num in nums[1:]:
            # If the next number is not same as prev and count becomes 0 make
            # this number as majority element and initialize count to 1 again
            # else just decrease the count
            if num != result:
                # decrease count by 1
                count -= 1
                # Make this element as majority element
                if count == 0:
                    result = num
                    count = 1
            else:
                # This is same element as previous one.
                count += 1
        return result


def check(expected, *args):
    classes = [SolutionA, SolutionB]
    for Solution in classes:
        print(Solution.__name__, expected)
        result = Solution().majorityElement(*args)
        print(result == expected)


if __name__ == "__main__":
    nums = [3, 2, 3]
    expect = 3
    check(expect, nums)

    nums = [2, 1, 1, 2, 1, 2, 2]
    expect = 2
    check(expect, nums)
