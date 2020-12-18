"""
278. First Bad Version

URL: https://leetcode.com/problems/first-bad-version/
Level: Easy
"""
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    bad = 4
    if version >= bad:
        return True
    else:
        return False

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # バイナリサーチ O(logn)
        low = 1
        high = n

        while low < high:
            mid = low + (high - low) //2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1

        return low


if __name__ == '__main__':
    sol = Solution()
    n = 5
    print(sol.firstBadVersion(5))