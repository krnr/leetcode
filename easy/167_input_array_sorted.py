"""
Given a 1-indexed array of integers numbers that is already sorted in
non-decreasing order, find two numbers such that they add up to a specific
target number. Let these two numbers be numbers[index1] and numbers[index2]
where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an
integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not
use the same element twice.

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

Constraints:

2 <= numbers.length <= 3 * 10^4
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
"""
from typing import *


class SolutionA:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def correct_sum(x, y):
            return numbers[x] + numbers[y] == target

        slow, fast = 0, 1
        for i in range(len(numbers)):
            slow = i
            fast = slow + 1
            if correct_sum(fast, slow):
                return [slow + 1, fast + 1]
            if numbers[slow] == numbers[fast]:
                continue
            while fast < len(numbers):
                if correct_sum(fast, slow):
                    return [slow + 1, fast + 1]
                fast += 1


class SolutionB:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def correct_sum(x, y):
            return numbers[x] + numbers[y] == target

        left, rght = 0, len(numbers) - 1
        while left < rght:
            if correct_sum(left, rght):
                return [left + 1, rght + 1]
            if numbers[left] + numbers[rght] > target:
                rght -= 1
            else:
                left += 1


def check(expected, nums, target):
    classes = [SolutionA, SolutionB]
    for Solution in classes:
        print(Solution.__name__, nums)
        result = Solution().twoSum(nums, target)
        print(result, result == expected)


if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    expect = [1, 2]
    check(expect, nums, target)

    nums = [2,3,4]
    target = 6
    expect = [1,3]
    check(expect, nums, target)

    nums = [-1,0]
    target = -1
    expect = [1, 2]
    check(expect, nums, target)

    nums = [0,0,3,4]
    target = 0
    expect = [1, 2]
    check(expect, nums, target)

    nums = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,3,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]
    target = 5
    expect = [61, 62]
    check(expect, nums, target)

