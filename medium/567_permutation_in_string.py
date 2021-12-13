"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 10^4
s1 and s2 consist of lowercase English letters.
"""
import string
from collections import Counter


class SolutionA:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        to_check = Counter(s1)
        start, finish = 0, len(s2) - len(s1) + 1
        while start < finish:
            substring = s2[start : start + len(s1)]
            if Counter(substring) == to_check:
                return True
            start += 1
        return False


# 56 vs 1440 ms!
class SolutionB:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def freq_dict(s: str):
            freq = {ltr: 0 for ltr in string.ascii_lowercase}
            for letter in s:
                freq[letter] += 1
            return freq

        target = freq_dict(s1)
        start, window = 0, len(s1)

        to_check = freq_dict(s2[start:window])
        while window < len(s2):
            if to_check == target:
                return True
            to_check[s2[start]] -= 1
            to_check[s2[window]] += 1
            start += 1
            window += 1
        return target == to_check


def check(expected, s1, s2):
    classes = [SolutionA, SolutionB]
    for Solution in classes:
        print(Solution.__name__, s1, s2)
        result = Solution().checkInclusion(s1, s2)
        print(result, result == expected)


if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"
    expect = True
    check(expect, s1, s2)

    s1 = "ab"
    s2 = "eidboaoo"
    expect = False
    check(expect, s1, s2)

    s1 = "adc"
    s2 = "dcda"
    expect = True
    check(expect, s1, s2)
