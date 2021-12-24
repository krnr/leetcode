""" 
Given a positive integer n, generate an n x n matrix filled with elements from
1 to n2 in spiral order.

Example 1:

Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]

Constraints:

1 <= n <= 20
"""
from typing import *


class SolutionA:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for _ in range(n)] for _ in range(n)]

        def get_direction(order: int):
            return ((0, 1), (1, 0), (0, -1), (-1, 0))[order % 4]

        dir = 0
        x, y = 0, 0
        num = 1
        for _ in range(1, n * n + 1):
            result[x][y] = num
            num += 1
            dx, dy = get_direction(dir)
            new_x = x + dx
            new_y = y + dy
            if new_x < n and new_y < n and not result[new_x][new_y]:
                x, y = new_x, new_y
            else:
                # cannot write next address - must rotate
                dir += 1
                dx, dy = get_direction(dir)
                x, y = x + dx, y + dy
        return result


class SolutionB:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for _ in range(n)] for _ in range(n)]
        top, btm = 0, n - 1
        left, rght = 0, n - 1

        num = 1
        while left <= rght and top <= btm:
            # top row
            for i in range(left, rght + 1):
                result[top][i] = num
                num += 1
            top += 1
            # right column
            for i in range(top, btm + 1):
                result[i][rght] = num
                num += 1
            rght -= 1
            # bottom row
            for i in range(rght, left - 1, -1):
                result[btm][i] = num
                num += 1
            btm -= 1
            # left column
            for i in range(btm, top - 1, -1):
                result[i][left] = num
                num += 1
            left += 1
        return result


def check(expected, n):
    classes = [SolutionA, SolutionB]
    for Solution in classes:
        print(Solution.__name__, expected)
        result = Solution().generateMatrix(n)
        print(result, result == expected)


if __name__ == "__main__":
    n = 3
    expect = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    check(expect, n)

    n = 1
    expect = [[1]]
    check(expect, n)

    n = 4
    expect = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
    check(expect, n)
