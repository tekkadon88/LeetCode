"""
27. Remove Element

URL: https://leetcode.com/problems/remove-element/
Level: Easy
"""
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            if nums[0] == val:
                return 0
            else:
                return 1

        i = 0
        j = len(nums) -1
        
        while i < j:
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                i += 1
        
        print(nums, i, j)
        if nums[i] == val:
            return i
        else:
            return i+1

if __name__ == '__main__':
    solution = Solution()
    nums = [3,2,2,3]
    val = 3
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    nums = [3,3]
    val =3
    print(solution.removeElement(nums, val))