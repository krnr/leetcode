"""
You are given an m x n binary matrix grid. An island is a group of 1's
(representing land) connected 4-directionally (horizontal or vertical.) You may
assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:

Input: grid = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""
import collections
from typing import *


class SolutionA:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        heigth = len(grid)
        width = len(grid[0])
        max_area = 0
        neigh = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def build_island(row, col):
            if row < 0 or col < 0 or row >= heigth or col >= width or not grid[row][col]:
                return 0
            grid[row][col] = 0
            return 1 + sum(build_island(row + x, col + y) for x, y in neigh)

        for row in range(heigth):
            for col in range(width):
                if grid[row][col]:
                    island_area = build_island(row, col)
                    max_area = max(max_area, island_area)
        return max_area


class SolutionB:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        heigth = len(grid)
        width = len(grid[0])
        max_area = 0
        neigh = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def build_island(row, col):
            island = collections.deque()
            island.append((row, col))
            area = 0

            def visit(r,c):
                if 0 <= r < heigth and 0 <= c < width and grid[r][c]:
                    grid[r][c] = 0
                    island.append((r,c))

            while island:
                row, col = island.popleft()
                area += 1
                for x, y in neigh:
                    visit(row + x, col + y)
            return area

        for row in range(heigth):
            for col in range(width):
                if grid[row][col]:
                    grid[row][col] = 0
                    island_area = build_island(row, col)
                    max_area = max(max_area, island_area)
        return max_area


def check(expected, grid):
    classes = [SolutionB]
    for Solution in classes:
        print(Solution.__name__, grid)
        result = Solution().maxAreaOfIsland(grid)
        print(result, result == expected)


if __name__ == "__main__":
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
    expect = 6
    check(expect, grid)

    grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
    expect = 0
    check(expect, grid)

    grid = [
        [0,0,0,0,1,1,1,0,0,1,1,0,1,0,1,1,1,0,0,1,0,0,1,0,1,0,0,0,1,1,0,0,0,1,0,1,1,1,1],
        [0,0,0,0,0,1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,1,0,0,1,0,1,1,0],
        [0,0,1,1,1,0,1,1,0,0,0,0,1,1,1,0,1,0,1,0,1,1,1,0,0,1,1,1,0,0,0,0,0,1,1,1,1,0,1],
        [0,1,0,0,1,1,0,1,0,1,1,0,1,0,1,0,0,1,0,0,0,0,1,1,0,1,0,0,1,1,0,1,1,0,0,1,0,1,1],
        [1,0,0,1,1,0,1,0,0,0,0,1,1,0,1,1,0,0,1,1,1,0,0,0,1,1,0,0,0,1,0,0,1,0,1,1,0,0,1]
    ]
    expect = 14
    check(expect, grid)
