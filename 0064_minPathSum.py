"""
64. Minimum Path Sum

URL: https://leetcode.com/problems/minimum-path-sum/
Level: Medium
"""
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [ [0]*len(grid[0]) for _ in range(len(grid)) ]
        dp[0][0] = grid[0][0]

        for i in range(1, len(grid[0])):
            dp[0][i] = grid[0][i] + dp[0][i-1]
        for j in range(1, len(grid)):
            dp[j][0] = grid[j][0] + dp[j-1][0]

        for row in range(1, len(grid)):
            for col in range(1, len(grid[0])):
                dp[row][col] = min(dp[row][col-1], dp[row-1][col]) + grid[row][col]

        # print(dp)
        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(solution.minPathSum(grid))
        