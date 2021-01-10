"""
107. Binary Tree Level Order Traversal II

URL: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
Level: Easy
"""
from typing import List
from queue import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ans = []
        next_level = deque([root])

        while root and next_level:
            curr = next_level
            next_level = deque()
            ans.append([])

            for node in curr:
                ans[-1].append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
        
        return ans[::-1]

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(solution.levelOrderBottom(root))