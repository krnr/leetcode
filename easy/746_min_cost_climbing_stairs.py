"""
You are given an integer array cost where cost[i] is the cost of ith step on a
staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999
"""
from typing import *


class SolutionA:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        paths = []
        length = len(cost)
        if length > 2:
            paths = [cost[0], cost[1]]
            for i in range(2, length):
                cost_for_step = cost[i] + min(paths[-1], paths[-2])
                paths.append(cost_for_step)
            return min(paths[-2], paths[-1])
        return min(cost)


class SolutionDP:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        dp = [0] * (length + 2)
        for i in range(length - 1, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        # [6, 105, 5, 5, 4, 102, 3, 2, 100, 1, 0, 0]
        return min(dp[0], dp[1])


def check(expected, *args):
    classes = [SolutionA, SolutionDP]
    for Solution in classes:
        print(Solution.__name__, expected)
        result = Solution().minCostClimbingStairs(*args)
        print(result, result == expected)


if __name__ == "__main__":
    cost = [10, 15, 20]
    expect = 15
    check(expect, cost)

    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    expect = 6
    check(expect, cost)
