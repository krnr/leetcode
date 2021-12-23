"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:

Input: rowIndex = 0
Output: [1]

Example 3:

Input: rowIndex = 1
Output: [1,1]

Constraints:

0 <= rowIndex <= 33

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
"""
from typing import *

"""
1
1 2
1 3 .
1 4 6
1 5 10 .
  6 15 20
  7 21 35
"""


class SolutionA:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]

        row = [0] * (rowIndex + 1)
        row[0] = 1
        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):
                row[j] = row[j] + row[j - 1]

        return row


def check(expected, *args):
    classes = [SolutionA]
    for Solution in classes:
        print(Solution.__name__, expected)
        result = Solution().getRow(*args)
        print(result, result == expected)


if __name__ == "__main__":
    rowIndex = 3
    expect = [1, 3, 3, 1]
    check(expect, rowIndex)

    rowIndex = 7
    expect = [1, 7, 21, 35, 21, 7, 1]
    check(expect, rowIndex)

    rowIndex = 0
    expect = [1]
    check(expect, rowIndex)

    rowIndex = 1
    expect = [1, 1]
    check(expect, rowIndex)
