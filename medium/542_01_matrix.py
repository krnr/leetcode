"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 10^4
1 <= m * n <= 10^4
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
"""
import collections
from typing import *


class SolutionA:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        heigth, width = len(mat), len(mat[0])
        rotations = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        max_val = 10000000000
        distances = [[max_val for col in row] for row in mat]

        def collect_zeros(matrix, dist):
            queue = collections.deque()
            for x, row in enumerate(matrix):
                for y, col in enumerate(row):
                    if not col:
                        queue.append((x, y))
                        dist[x][y] = 0
            return queue

        # we can mark else: mat[x][y] = -1 to save space not using another matrix

        queue = collect_zeros(mat, distances)

        def inbound(row, col):
            return row >= 0 and row < heigth and col >= 0 and col < width

        while queue:
            row, col = queue.popleft()
            for x, y in rotations:
                new_r, new_c = row + x, col + y
                if inbound(new_r, new_c):
                    to_current = distances[row][col] + 1
                    if distances[new_r][new_c] > to_current:
                        distances[new_r][new_c] = to_current
                        queue.append((new_r, new_c))

        return distances


class SolutionDP:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        heigth, width = len(mat), len(mat[0])
        max_val = 10000000000

        for x, row in enumerate(mat):
            for y, value in enumerate(row):
                if value:
                    top = mat[x - 1][y] if x > 0 else max_val
                    left = mat[x][y - 1] if y > 0 else max_val
                    mat[x][y] = min(top, left) + 1

        for x in range(heigth - 1, -1, -1):
            for y in range(width - 1, -1, -1):
                value = mat[x][y]
                if value:
                    bottom = mat[x + 1][y] if x + 1 < heigth else max_val
                    right = mat[x][y + 1] if y + 1 < width else max_val
                    mat[x][y] = min(value, bottom + 1, right + 1)
        return mat


def check(expected, matrix):
    classes = [SolutionA, SolutionDP]
    for Solution in classes:
        print(Solution.__name__, matrix)
        result = Solution().updateMatrix(matrix)
        print(result, result == expected)


if __name__ == "__main__":
    mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    expect = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    check(expect, mat)

    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    expect = [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
    check(expect, mat)
