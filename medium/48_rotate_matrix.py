"""
You are given an n x n 2D matrix representing an image, rotate the image by 90
degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input
2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""
from typing import *


class SolutionA:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        height, width = len(matrix), len(matrix[0])
        # first rotation: top and bottom
        # [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
        for i in range(height // 2):
            btm = -1 - i
            for j in range(width):
                matrix[i][j], matrix[btm][j] = matrix[btm][j], matrix[i][j]
        # now swap diagonal
        """
        7 8 9  7 4 9  7 4 1  7 4 1
        4 5 6  8 5 6  8 5 6  8 5 2
        1 2 3  1 2 3  9 2 3  9 6 3

               [0][1] [0][2] [1][2]
               [1][0] [2][0] [2][1]
        """
        for i in range(height):
            for j in range(i + 1, width):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def check(expected, A):
    classes = [SolutionA]
    for Solution in classes:
        A = list(A)
        print(Solution.__name__, expected)
        Solution().rotate(A)
        print(A, A == expected)


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expect = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    check(expect, matrix)

    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    expect = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
    check(expect, matrix)
