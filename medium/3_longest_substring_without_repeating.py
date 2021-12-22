"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:

Input: s = ""
Output: 0
 
Constraints:

0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.

"""
from typing import *


class SolutionA:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        current = ""
        for letter in s:
            if letter in current:
                longest = max(longest, len(current))
                current = current[current.find(letter) + 1 :] + letter
            else:
                current += letter
        return max(longest, len(current))


class SolutionB:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = longest = 0
        used_chars = {}
        for idx, char in enumerate(s):
            if char in used_chars:
                previous_position = used_chars[char]
                # was char seen in the current sequence?
                if start <= previous_position:
                    # ...now we must start next sequence
                    start = previous_position + 1
            else:
                longest = max(longest, idx - start + 1)
            used_chars[char] = idx
        return longest


def check(expected, s):
    classes = [SolutionA, SolutionB]
    for Solution in classes:
        print(Solution.__name__, s)
        result = Solution().lengthOfLongestSubstring(s)
        print(result, result == expected)


if __name__ == "__main__":
    s = "abcabcbb"
    expect = 3
    check(expect, s)

    s = "bbbbb"
    expect = 1
    check(expect, s)

    s = "pwwkew"
    expect = 3
    check(expect, s)

    s = ""
    expect = 0
    check(expect, s)

    s = " "
    expect = 1
    check(expect, s)

    s = "dvdf"
    expect = 3
    check(expect, s)
