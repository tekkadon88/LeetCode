"""
28. Implement strStr()

URL: https://leetcode.com/problems/implement-strstr/
Level: Easy
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == 0:
            if len(needle) == 0:
                return 0
            else:
                return -1

        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

if __name__ == '__main__':
    solution = Solution()
    haystack = 'hello'
    needle = 'll'
    print(solution.strStr(haystack, needle))