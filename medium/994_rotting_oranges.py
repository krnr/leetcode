"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten
orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh
orange. If this is impossible, return -1.

Example 1:

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never
rotten, because rotting only happens 4-directionally.

Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""
import collections
from typing import *


class SolutionR:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        heigth, width = len(grid), len(grid[0])
        rotations = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def inbound(row, col):
            return row >= 0 and row < heigth and col >= 0 and col < width

        ripe, rotn = 1, 2

        to_check = []
        for x, row in enumerate(grid):
            for y, value in enumerate(row):
                if value == rotn:
                    to_check.append((x, y))

        def traverse(to_check, level=0):
            next_gen = []
            while to_check:
                row, col = to_check.pop()
                for x, y in rotations:
                    new_r, new_c = row + x, col + y
                    if inbound(new_r, new_c) and grid[new_r][new_c] == ripe:
                        next_gen.append((new_r, new_c))
                        grid[new_r][new_c] = rotn
            if next_gen:
                return traverse(next_gen, level + 1)

            for x, row in enumerate(grid):
                for y, value in enumerate(row):
                    if value == ripe:
                        return -1
            return level

        return traverse(to_check)


class SolutionB:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        heigth, width = len(grid), len(grid[0])
        rotations = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def inbound(row, col):
            return row >= 0 and row < heigth and col >= 0 and col < width

        ripe, rotn = 1, 2
        invalid = -1

        if not heigth:
            return invalid

        ripe_cnt = 0
        gen_passed = 0
        to_check = collections.deque()

        for x, row in enumerate(grid):
            for y, value in enumerate(row):
                if value == rotn:
                    to_check.append((x, y))
                if value == ripe:
                    ripe_cnt += 1

        while to_check and ripe_cnt:
            print(to_check)
            print(ripe_cnt, gen_passed)
            gen_passed += 1
            # must pop ALL cells for the current generation!
            for _ in range(len(to_check)):
                row, col = to_check.popleft()
                for x, y in rotations:
                    new_r, new_c = row + x, col + y
                    if inbound(new_r, new_c) and grid[new_r][new_c] == ripe:
                        to_check.append((new_r, new_c))
                        grid[new_r][new_c] = rotn
                        ripe_cnt -= 1

        return gen_passed if not ripe_cnt else invalid


def check(expected, matrix):
    classes = [SolutionB]
    for Solution in classes:
        print(Solution.__name__, matrix)
        result = Solution().orangesRotting(matrix)
        print(result, result == expected)


if __name__ == "__main__":
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    expect = 4
    check(expect, grid)

    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    expect = -1
    check(expect, grid)

    grid = [[0, 2]]
    expect = 0
    check(expect, grid)

    grid = [[0]]
    expect = 0
    check(expect, grid)

    grid = [[1], [0], [1]]
    expect = -1
    check(expect, grid)
