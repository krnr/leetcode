"""
Write an efficient algorithm that searches for a target value in an m x n
integer matrix. The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example 1:

Input: matrix = [
        [1,4,7,11,15],
        [2,5,8,12,19],
        [3,6,9,16,22],
        [10,13,14,17,24],
        [18,21,23,26,30]
], target = 5
Output: true

Example 2:

Input: matrix = [
        [1,4,7,11,15],
        [2,5,8,12,19],
        [3,6,9,16,22],
        [10,13,14,17,24],
        [18,21,23,26,30]
], target = 20
Output: false

Constraints:

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-10^9 <= matrix[i][j] <= 10^9
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-10^9 <= target <= 10^9
"""
from typing import *


class SolutionA:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        width = len(matrix[0])
        for row in matrix:
            n = row[0]
            if n > target:
                break
            for i in range(width):
                n = row[i]
                if n == target:
                    return True
                if n > target:
                    break
        return False


class SolutionB:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        width = len(matrix[0])

        x, y = len(matrix) - 1, 0
        # Start adaptive search from bottom left corner
        while True:
            if x < 0 or y >= width:
                break
            print("check", x, y)
            current = matrix[x][y]
            if current > target:  # go up
                x -= 1
            elif current < target:  # go right
                y += 1
            else:
                return True
        return False


def check(expected, *args):
    classes = [SolutionA, SolutionB]
    for Solution in classes:
        print(Solution.__name__, expected)
        found = Solution().searchMatrix(*args)
        print(found, found == expected)


if __name__ == "__main__":
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    target = 20
    expect = False
    check(expect, matrix, target)

    target = 5
    expect = True
    check(expect, matrix, target)

    matrix = [[1, 1]]
    target = 2
    expect = False
    check(expect, matrix, target)
    matrix = [[-5]]
    target = -5
    expect = True
    check(expect, matrix, target)
