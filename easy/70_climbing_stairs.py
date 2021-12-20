"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:

1 <= n <= 45
"""


class SolutionA:
    def climbStairs(self, n: int) -> int:
        if not n:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        one_step_before = 1
        two_step_before = 2
        all_ways = 0
        i = 2
        while i < n:
            all_ways = one_step_before + two_step_before
            two_step_before = one_step_before
            one_step_before = all_ways
            i += 1

        return all_ways


from functools import lru_cache


class SolutionB:
    @lru_cache(None)
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


def check(expected, *args):
    classes = [SolutionA, SolutionB]
    for Solution in classes:
        print(Solution.__name__, expected)
        result = Solution().climbStairs(*args)
        print(result)


if __name__ == "__main__":
    n = 2
    expect = 2
    check(expect, n)

    n = 3
    expect = 3
    check(expect, n)

    n = 4
    expect = 5
    check(expect, n)
