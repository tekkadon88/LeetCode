"""
108. Convert Sorted Array to Binary Search Tree

URL: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
Level: Easy
"""
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None
            p = left + (right - left) //2

            root = TreeNode(nums[p])
            root.left = helper(left, p-1)
            root.right = helper(p+1, right)
            return root

        return helper(0, len(nums)-1)

if __name__ == '__main__':
    solution = Solution()
    nums = [-10,-3,0,5,9]
    node = solution.sortedArrayToBST(nums)