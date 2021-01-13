"""
111. Minimum Depth of Binary Tree

URL: https://leetcode.com/problems/minimum-depth-of-binary-tree/
Level: Easy
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def helper(node):
            if node is None:
                return 0

            if node.left and node.right:
                return 1+ min(helper(node.left), helper(node.right))
            elif node.left:
                return 1+ helper(node.left)
            elif node.right:
                return 1+ helper(node.right)
            else:
                return 1

        return helper(root)

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    #root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(5)), TreeNode(6)), TreeNode(10))
    print(solution.minDepth(root))

        