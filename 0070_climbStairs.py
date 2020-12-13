"""
70. Climbing Stairs

URL: https://leetcode.com/problems/climbing-stairs/
Level: Easy
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        # base case
        if n == 1 or n == 2:
            return n
        
        # dpテーブルを用意して、n=1とn=2で初期化
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        
        # i番目にくるにはi-1番目から１ステップか、
        # i-2番目から２ステップなので、両方を足し合わせたものを求めればいい
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]

if __name__ == '__main__':
    solution = Solution()
    n = 4
    print(solution.climbStairs(n))