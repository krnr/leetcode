"""
Flood Fill.

An image is represented by a 2-D array of integers, each integer representing the 
pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the 
flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 
4-directionally to the starting pixel of the same color as the starting pixel, plus 
any pixels connected 4-directionally to those pixels (also with the same color as the
starting pixel), and so on. Replace the color of all of the aforementioned pixels with
the newColor.

At the end, return the modified image.

Example 1:

Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2

Output: [[2,2,2],[2,2,0],[2,0,1]]

Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].


  1  1  1
  1  1  0
  1  0  1
"""
from typing import *

Image = List[List[int]]

visited, to_visit = set(), set()


class FloodFill:
    def __init__(self, image: Image, sr: int, sc: int, new_color: int) -> Image:
        self.image = image
        self.start_row = sr
        self.start_col = sc
        self.new_color = new_color
        self.old_color = image[sr][sc]
        self._total_rows = len(image)
        self._total_cols = len(image[0])

    def main(self) -> Image:
        to_visit.add((self.start_row, self.start_col))
        while to_visit:
            self.lookup()
        while visited:
            x, y = visited.pop()
            self.paint(x, y)
        return self.image

    def paint(self, row, col):
        self.image[row][col] = self.new_color

    def up(self, row, col):
        return self.image[row - 1][col]

    def right(self, row, col):
        return self.image[row][col + 1]

    def down(self, row, col):
        return self.image[row + 1][col]

    def left(self, row, col):
        return self.image[row][col - 1]

    def lookup(self):
        row, col = to_visit.pop()
        left = (row, col - 1)
        up = (row - 1, col)
        right = (row, col + 1)
        down = (row + 1, col)
        if row > 0 and self.up(row, col) == self.old_color and up not in visited:
            to_visit.add(up)
        if (
            row < self._total_rows - 1
            and self.down(row, col) == self.old_color
            and down not in visited
        ):
            to_visit.add(down)
        if (
            col < self._total_cols - 1
            and self.right(row, col) == self.old_color
            and right not in visited
        ):
            to_visit.add(right)
        if col > 0 and self.left(row, col) == self.old_color and left not in visited:
            to_visit.add(left)
        visited.add((row, col))


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr, sc = 1, 1
new_image = 100

FloodFill(image, sr, sc, new_image).main()


class FastestSolution:
    def floodFill(self, image: Image, sr: int, sc: int, newColor: int) -> Image:
        if not image or len(image) == 0:
            return 0
        m = len(image)
        n = len(image[0])
        neighs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        # [[1,0],[-1,0],[0,1],[0,-1]]

        def bfs(row, col, oldColor):
            q = [[row, col]]
            while q:
                x, y = q.pop(0)
                for neigh in neighs:
                    x = row + neigh[0]
                    y = col + neigh[1]
                    if (
                        x < m
                        and x >= 0
                        and y < n
                        and y >= 0
                        and image[x][y] == oldColor
                    ):
                        image[x][y] = newColor
                        bfs(x, y, oldColor)

        if image[sr][sc] == newColor:
            return image
        else:
            oldColor = image[sr][sc]
            image[sr][sc] = newColor
            bfs(sr, sc, oldColor)
            return image


class MemoryOptimalSolution:
    def floodFill(self, image: Image, sr: int, sc: int, newColor: int) -> Image:
        if image[sr][sc] == newColor:
            return image

        def adjacent_flood(sr, sc):
            adjacent = (sr - 1, sc), (sr + 1, sc), (sr, sc - 1), (sr, sc + 1)
            for x, y in adjacent:
                if (
                    (x >= 0)
                    and (x < len(image))
                    and (y >= 0)
                    and (y < len(image[0]))
                    and (image[x][y] == color)
                ):
                    image[x][y] = newColor
                    adjacent_flood(x, y)

        color = image[sr][sc]
        image[sr][sc] = newColor

        adjacent_flood(sr, sc)

        return image


class DFSSolution(object):
    def floodFill(self, image, sr, sc, newColor):
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image

        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1:
                    dfs(r - 1, c)
                if r + 1 < R:
                    dfs(r + 1, c)
                if c >= 1:
                    dfs(r, c - 1)
                if c + 1 < C:
                    dfs(r, c + 1)

        dfs(sr, sc)
        return image

