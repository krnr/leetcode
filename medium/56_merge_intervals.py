"""
Given an array of intervals where intervals[i] = [starti, endi], merge all
overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 
Constraints:

1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^4
"""
from typing import *


class SolutionA:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()
        current = intervals[0]
        for start, end in intervals[1:]:
            if start <= current[1] and end >= current[0]:
                current = [min(start, current[0]), max(end, current[1])]
            else:
                result.append(current)
                current = [start, end]
        result.append(current)
        return result


class SolutionB:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()
        idx, length = 0, len(intervals)
        while idx < length:
            start, end = intervals[idx]
            idx += 1
            while idx < length and intervals[idx][0] <= end:
                end = max(end, intervals[idx][1])
                idx += 1
            result.append([start, end])
        return result


def check(expected, *args):
    classes = [SolutionA, SolutionB]
    for Solution in classes:
        print(Solution.__name__, expected)
        solution = Solution().merge(*args)
        print(solution, solution == expected)


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    expect = [[1, 6], [8, 10], [15, 18]]
    check(expect, intervals)

    intervals = [[1, 4], [4, 5]]
    expect = [[1, 5]]
    check(expect, intervals)

    intervals = [[1, 4], [0, 4]]
    expect = [[0, 4]]
    check(expect, intervals)

    intervals = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
    expect = [[1, 10]]
    check(expect, intervals)
