"""
Given an array of intervals intervals where intervals[i] = [starti, endi],
return the minimum number of intervals you need to remove to make the rest of
the intervals non-overlapping.

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Constraints:

1 <= intervals.length <= 10^5
intervals[i].length == 2
-5 * 10^4 <= starti < endi <= 5 * 10^4
"""
from typing import *


class SolutionA:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[-1])

        to_remove = 0
        previous = intervals[0]
        for i in range(1, len(intervals)):
            current = intervals[i]
            if previous[1] > current[0]:
                to_remove += 1
            else:
                previous = current
        return to_remove


def check(expected, *args):
    classes = [SolutionA]
    for Solution in classes:
        print(Solution.__name__, expected)
        solution = Solution().eraseOverlapIntervals(*args)
        print(solution, solution == expected)


if __name__ == "__main__":
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    expect = 1
    check(expect, intervals)

    intervals = [[1, 2], [1, 2], [1, 2]]
    expect = 2
    check(expect, intervals)

    intervals = [[1, 2], [2, 3]]
    expect = 0
    check(expect, intervals)
