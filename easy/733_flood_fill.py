"""
An image is represented by an m x n integer grid image where image[i][j]
represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a
flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected
4-directionally to the starting pixel of the same color as the starting pixel,
plus any pixels connected 4-directionally to those pixels (also with the same
color), and so on. Replace the color of all of the aforementioned
pixels with newColor.

Return the modified image after performing the flood fill.

Example 1:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1)
(i.e., the red pixel), all pixels connected by a path of the same color as the
starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally
connected to the starting pixel.

Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
Output: [[2,2,2],[2,2,2]]

Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], newColor < 2^16
0 <= sr < m
0 <= sc < n
"""
from typing import *


class SolutionB:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        heigth = len(image)
        width = len(image[0])
        visited = []
        to_color = []
        to_visit = [(sr, sc)]
        base_color = image[sr][sc]

        def is_in_fill(row, col):
            return image[row][col] == base_color

        def visit_south(row, col):
            if row + 1 < heigth and is_in_fill(row + 1, col):
                new_cell = (row + 1, col)
                if new_cell not in visited:
                    to_visit.append(new_cell)

        def visit_north(row, col):
            if row > 0 and is_in_fill(row - 1, col):
                new_cell = (row - 1, col)
                if new_cell not in visited:
                    to_visit.append(new_cell)

        def visit_east(row, col):
            if col > 0 and is_in_fill(row, col - 1):
                new_cell = (row, col - 1)
                if new_cell not in visited:
                    to_visit.append(new_cell)

        def visit_west(row, col):
            if col + 1 < width and is_in_fill(row, col + 1):
                new_cell = (row, col + 1)
                if new_cell not in visited:
                    to_visit.append(new_cell)

        while to_visit:
            print(to_visit, to_color)
            x, y = to_visit.pop()
            if (x, y) in visited:
                continue
            to_color.append((x, y))
            visit_south(x, y)
            visit_north(x, y)
            visit_east(x, y)
            visit_west(x, y)
            visited.append((x, y))

        def color_image(color):
            while to_color:
                row, col = to_color.pop()
                image[row][col] = color

        color_image(newColor)
        return image


class SolutionD:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        heigth = len(image)
        width = len(image[0])
        base_color = image[sr][sc]

        def dfs(row, col):
            if row < 0 or row >= heigth or col < 0 or col >= width:
                return
            current_color = image[row][col]
            if current_color != base_color or current_color == newColor:
                return

            image[row][col] = newColor
            print("colored", row, col)

            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dfs(row + x, col + y)

        dfs(sr, sc)
        return image


def check(expected, image, sr, sc, new_color):
    classes = [SolutionD]
    for Solution in classes:
        print(Solution.__name__, image, sr, sc, new_color)
        result = Solution().floodFill(image, sr, sc, new_color)
        print(result, result == expected)


if __name__ == "__main__":
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2
    expect = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    check(expect, image, sr, sc, newColor)

    image = [[0, 0, 0], [0, 0, 0]]
    sr = 0
    sc = 0
    newColor = 2
    expect = [[2, 2, 2], [2, 2, 2]]
    check(expect, image, sr, sc, newColor)
