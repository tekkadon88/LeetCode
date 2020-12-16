"""
35. Search Insert Position

URL: https://leetcode.com/problems/search-insert-position/
Level: Easy
"""
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        バイナリサーチでターゲットを探す
        '''
        low = 0
        high = len(nums)-1
        
        while low <= high:
            mid = low + (high - low)//2

            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                high = mid -1
            
            if nums[mid] < target:
                low = mid +1
                
        return low
        
if __name__ == '__main__':
    solution = Solution()
    nums = [1,3,5,6]
    target = 5
    print(solution.searchInsert(nums, target))