"""
112. Path Sum

URL: https://leetcode.com/problems/path-sum/
Level: Easy
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def helper(node, target):
            if node is None:
                return False
            
            target -= node.val

            if not node.left and not node.right: # leaf
                return target == 0

            return helper(node.left, target) or helper(node.right, target)
        
        return helper(root, sum)

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    # target = 30 # true
    # target = 12 # true
    target = 11 # false
    print(solution.hasPathSum(root, target))