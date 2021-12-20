"""
Given a string s, we can transform every letter individually to be lowercase or
uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]

Example 3:

Input: s = "12345"
Output: ["12345"]

Example 4:

Input: s = "0"
Output: ["0"]

Constraints:

s will be a string with length between 1 and 12.
s will consist only of letters or digits.
"""
from typing import *
import itertools as it


class SolutionA:
    def letterCasePermutation(self, s: str) -> List[str]:
        results = []
        for pos, letter in enumerate(s):
            if letter.isalpha():
                results.append((letter.lower(), pos))
        if not results:
            return {s}
        else:
            return self.dfs(s, results, set())

    def dfs(self, s, positions, permutations):
        if not positions:
            return permutations
        letter, pos = positions.pop()
        if permutations:
            # do not iterate over appended
            length = len(permutations)
            perms = list(permutations)
            for i in range(length):
                perm = perms[i]
                permutations.add(perm[:pos] + letter.upper() + perm[pos + 1 :])
                permutations.add(perm[:pos] + letter.lower() + perm[pos + 1 :])
        else:
            permutations.add(s[:pos] + letter.upper() + s[pos + 1 :])
            permutations.add(s[:pos] + letter.lower() + s[pos + 1 :])
        return self.dfs(s, positions, permutations)


class SolutionB:
    def letterCasePermutation(self, s: str) -> List[str]:
        results = []
        max_length = len(s)
        def dfs(temp_s, idx):
            if len(temp_s) == max_length:
                # we're over building the string
                results.append(temp_s)
                return

            letter = s[idx]
            if letter.isalpha():
                # append two run branches to current
                dfs(temp_s + letter.lower(), idx + 1)
                dfs(temp_s + letter.upper(), idx + 1)
            else:
                # append numeric to current branch
                dfs(temp_s + letter, idx + 1)

        dfs("", 0)
        return results


def check(expected, *args):
    classes = [SolutionA, SolutionB]
    for Solution in classes:
        print(Solution.__name__, expected)
        result = Solution().letterCasePermutation(*args)
        print(result)


if __name__ == "__main__":
    s = "a1b2"
    expect = ["a1b2", "a1B2", "A1b2", "A1B2"]
    check(expect, s)

    s = "3z4"
    expect = ["3z4", "3Z4"]
    check(expect, s)

    s = "12345"
    expect = ["12345"]
    check(expect, s)

    s = "0"
    expect = ["0"]
    check(expect, s)
