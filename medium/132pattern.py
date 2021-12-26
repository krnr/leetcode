"""
Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence
ai, aj, ak such that i < j < k and ai < ak < aj.
Design an algorithm that takes a list of n numbers as input and checks whether
there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]
Output: False
Explanation: There is no 132 pattern in the sequence.

Example 2:
Input: [3, 1, 4, 2]
Output: True
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:
Input: [-1, 3, 2, 0]
Output: True
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
"""

from collections import deque


class SolutionA:
    def find132pattern(self, nums) -> bool:
        length = len(nums)
        if length < 3:
            return False

        stack_ = deque()
        last_min = float("-inf")
        for i in range(1, length + 1):
            current = nums[-i]
            if current < last_min:
                return True
            while stack_ and stack_[-1] < current:
                last_min = stack_.pop()
            stack_.append(current)
        return False


def check(expected, n):
    classes = [SolutionA]
    for Solution in classes:
        print(Solution.__name__, expected)
        result = Solution().find132pattern(n)
        print(result, result == expected)


if __name__ == "__main__":
    nums = [3, 5, 0, 3, 4]
    expect = True
    check(expect, nums)
