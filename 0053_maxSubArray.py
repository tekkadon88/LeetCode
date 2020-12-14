"""
53. Maximum Subarray

URL: https://leetcode.com/problems/maximum-subarray/
Level: Easy
"""
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = [float('-inf')] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0]+nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
        
        return max(dp)

if __name__ == '__main__':
    solution = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(solution.maxSubArray(nums))