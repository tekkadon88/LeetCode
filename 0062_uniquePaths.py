"""
62. Unique Paths

URL: https://leetcode.com/problems/unique-paths/
Level: Medium
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [ [0]*n for _ in range(m) ]

        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        # print(dp)
        return dp[m-1][n-1]

if __name__ == '__main__':
    solution = Solution()
    m = 3
    n = 3
    print(solution.uniquePaths(m, n))