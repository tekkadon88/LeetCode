"""
113. Path Sum II

URL: https://leetcode.com/problems/path-sum-ii/
Level: Medium
"""
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []
        tmp = []

        def helper(node, target, arr):
            nonlocal ans

            if node is None:
                return
            
            target -= node.val
            tmp.append(node.val)

            if node.left is None and node.right is None: # leaf
                if target == 0:
                    ans.append(list(tmp))
            else:
                helper(node.left, target, tmp)
                helper(node.right, target, tmp)
            
            tmp.pop()
   
        helper(root, sum, tmp)

        return ans

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
    target = 22 # true
    print(solution.pathSum(root, target))