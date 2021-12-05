"""
You are a product manager and currently leading a team to develop a new
product. Unfortunately, the latest version of your product fails the quality
check. Since each version is developed based on the previous version, all the
versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first
bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version
is bad. Implement a function to find the first bad version. You should minimize
the number of calls to the API.

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:

Input: n = 1, bad = 1
Output: 1

Constraints:

1 <= bad <= n <= 2^31 - 1
"""


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        min_good = 1
        max_bad = n
        while max_bad > min_good:
            current = (max_bad - min_good) // 2 + min_good
            if isBadVersion(current):
                max_bad = current
            else:
                min_good = current + 1
        return max_bad


class SolutionManual:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        last_good = 0
        last_bad = n
        current = n // 2
        while last_bad >= last_good:
            if isBadVersion(current):
                print(current, "is bad")
                if last_bad - last_good == 1 or last_bad == 1:
                    print(last_bad, "is the answer")
                    return last_bad
                last_bad = current
                current = (last_bad + last_good) // 2
            else:
                print(current, "is good")
                if last_bad - last_good == 1:
                    print(last_bad, "is the answer")
                    return last_bad

                last_good = current
                current = (n + last_good) // 2
        return last_bad
