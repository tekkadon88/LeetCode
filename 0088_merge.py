"""
88. Merge Sorted Array

URL: https://leetcode.com/problems/merge-sorted-array/
Level: Easy
"""
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m -1
        j = n -1

        for k in range(m+n-1, -1, -1):
            v1 = nums1[i] if i >=0 else float('-inf')
            v2 = nums2[j] if j >=0 else float('-inf')

            if v1 > v2:
                nums1[k] = v1
                i -= 1
            else:
                nums1[k] = v2
                j -= 1
        
        print(nums1)


if __name__ == '__main__':
    solution = Solution()
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    m = 3
    n = 3
    print(solution.merge(nums1, m, nums2, n))