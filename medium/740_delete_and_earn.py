"""
You are given an integer array nums. You want to maximize the number of points
you get by performing the following operation any number of times:

- Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must
delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
- Return the maximum number of points you can earn by applying the above
operation some number of times.

Example 1:

Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.

Example 2:

Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.

Constraints:

1 <= nums.length <= 2 * 10^4
1 <= nums[i] <= 10^4
"""
from collections import Counter
from typing import *


class SolutionA:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0

        freq = Counter(nums)
        keys = sorted(freq.keys())

        def points_for(key: int) -> int:
            return key * freq[key]

        previous = 0
        current_points = points_for(keys[0])
        for i in range(1, len(keys)):
            this = keys[i]
            if this - keys[i - 1] == 1:
                previous, current_points = current_points, max(current_points, previous + points_for(this))
            else:
                previous, current_points = current_points, current_points + points_for(this)
        return current_points


class SolutionB:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        The order of nums does not matter.
        Once we decide that we want a num, we can add all the occurrences of
        num into the total. We first transform the nums array into a points
        array that sums up the total number of points for that particular
        value. A value of x will be assigned to index x in points.

        nums: [2, 2, 3, 3, 3, 4]
        (2 appears 2 times, 3 appears 3 times, 4 appears once)
        points: [0, 0, 4, 9, 4] <- This is the gold in each house!
        """
        freq = Counter(nums)
        prev, curr = 0, 0
        for i in range(max(freq.keys()) + 1):
            prev, curr = curr, max(curr, prev + freq[i] * i)
        return curr


def check(expected, *args):
    classes = [SolutionA,SolutionB]
    for Solution in classes:
        print(Solution.__name__, expected)
        result = Solution().deleteAndEarn(*args)
        print(result, result == expected)


if __name__ == "__main__":
    nums = [3, 4, 2]
    expect = 6
    check(expect, nums)

    nums = [2, 2, 3, 3, 3, 4]
    expect = 9
    check(expect, nums)
