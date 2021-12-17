"""
Given two integers n and k, return all possible combinations of k numbers out
of the range [1, n].

You may return the answer in any order.

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]

Constraints:

1 <= n <= 20
1 <= k <= n
"""
import itertools as it
from typing import *


class SolutionA:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(it.combinations(range(1, n + 1), k))


class SolutionB:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = [[]]
        for rounds in range(k, 0, -1):
            combinations = [
                [i] + c
                for c in combinations
                for i in range(rounds, c[0] if c else n + 1)
            ]
        return combinations


def check(expected, n, k):
    classes = [SolutionA, SolutionB]
    for Solution in classes:
        print(Solution.__name__, expected)
        result = Solution().combine(n, k)
        print(result)


if __name__ == "__main__":
    n = 4
    k = 2
    expect = [
        [2, 4],
        [3, 4],
        [2, 3],
        [1, 2],
        [1, 3],
        [1, 4],
    ]
    check(expect, n, k)

    n = 4
    k = 3
    expect = [
        [2, 3, 4],
        [1, 3, 4],
        [1, 2, 3],
        [1, 2, 4],
    ]
    check(expect, n, k)

    n = 1
    k = 1
    expect = [[1]]
    check(expect, n, k)
