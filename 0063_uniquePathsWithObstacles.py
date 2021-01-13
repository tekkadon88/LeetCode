"""
63. Unique Paths II

URL: https://leetcode.com/problems/unique-paths-ii/
Level: Medium
"""
from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [ [0]*n for _ in range(m) ]

        if obstacleGrid[0][0] == 1:
            return 0

        i = 0
        count = 1
        while i < m:
            if obstacleGrid[i][0] == 1:
                count = 0
            dp[i][0] = count
            i += 1
        j = 0
        count = 1
        while j < n:
            if obstacleGrid[0][j] == 1:
                count = 0
            dp[0][j] = count
            j += 1
        
        for row in range(1, m):
            for col in range(1, n):
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                else:
                    dp[row][col] = dp[row-1][col] + dp[row][col-1]
        
        # print(dp)
        return dp[m-1][n-1]

if __name__ == '__main__':
    solution = Solution()
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    #obstacleGrid = [[0,1],[0,0]]
    #obstacleGrid = [[1,0]]
    print(solution.uniquePathsWithObstacles(obstacleGrid))