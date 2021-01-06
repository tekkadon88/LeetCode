"""
226. Invert Binary Tree

URL: https://leetcode.com/problems/invert-binary-tree/
Level: Easy
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        
        leftNode = self.invertTree(root.left)
        rightNode = self.invertTree(root.right)
        
        # if leftNode is not None and rightNode is not None:
        #     print(leftNode.val, rightNode.val)
        root.left = rightNode
        root.right = leftNode

        return root

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    node = solution.invertTree(root)        