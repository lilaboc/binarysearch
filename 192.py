# https://binarysearch.com/problems/Swap-Characters-to-Equalize-Strings

from collections import Counter


class Solution:
    def solve(self, s, t):
        for i in Counter(s + t).values():
            if i % 2 != 0:
                return False
        return True


# print(Solution().solve("ab", "ba"))
print(Solution().solve("aa", "bb"))
