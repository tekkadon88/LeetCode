"""
276. Paint Fence

URL: https://leetcode.com/problems/paint-fence/
Level: Easy
"""
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return k
        
        dp = [0] * (n+1)
        dp[1] = k
        dp[2] = k*k

        for i in range(3, n+1):
            dp[i] = (dp[i-1] + dp[i-2]) * (k-1)
        
        return dp[-1]
        


if __name__ == '__main__':
    solution = Solution()
    n = 3
    k = 2
    print(solution.numWays(n, k))