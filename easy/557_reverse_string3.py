"""
Given a string s, reverse the order of characters in each word within a
sentence while still preserving whitespace and initial word order.

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:

Input: s = "God Ding"
Output: "doG gniD"
 

Constraints:

1 <= s.length <= 5 * 10^4
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
"""
class SolutionA:
    def reverseWords(self, s: str) -> str:
        return " ".join(w[::-1] for w in s.split(" "))


def check(expected, s):
    classes = [SolutionA]
    for Solution in classes:
        n = list(s)
        print(Solution.__name__, expected)
        Solution().reverseWords(n)
        print(n, n == expected)


if __name__ == "__main__":
    s = "Let's take LeetCode contest"
    expect = "s'teL ekat edoCteeL tsetnoc"
    check(expect, s)

    s = "God Ding"
    expect = "doG gniD"
    check(expect, s)
