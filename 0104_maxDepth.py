"""
104. Maximum Depth of Binary Tree

URL: https://leetcode.com/problems/maximum-depth-of-binary-tree/
Level: Easy
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(node, depth):
            if node is None:
                return depth
            
            depth += 1
            return max(dfs(node.left, depth), dfs(node.right, depth))
        
        if root is None:
            return 0

        return dfs(root, 0)

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(solution.maxDepth(root))