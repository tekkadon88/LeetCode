"""
14. Longest Common Prefix

URL: https://leetcode.com/problems/longest-common-prefix/
Level: Easy
"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''

        prefix = strs[0]

        for word in strs[1:]:
            while prefix != '':
                if word.startswith(prefix):
                    break
                else:
                    prefix = prefix[0:len(prefix)-1]

        return prefix

if __name__ == '__main__':
    solution = Solution()
    strs = ["flower","flow","flight"]
    print(solution.longestCommonPrefix(strs))

    strs = ["dog","racecar","car"]
    print(solution.longestCommonPrefix(strs))