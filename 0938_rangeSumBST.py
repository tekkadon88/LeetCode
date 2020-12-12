"""
938. Range Sum of BST

URL: https://leetcode.com/problems/range-sum-of-bst/
Level: Easy
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        '''
        DFSでノードを探索
        '''
        def dfs(node):
            nonlocal total, low, high

            if node is None:
                return

            if low <= node.val <= high:
                total += node.val
                dfs(node.left)
                dfs(node.right)
            elif low > node.val:
                dfs(node.right)
            elif node.val > high:
                dfs(node.left)
        
        total = 0
        dfs(root)
        return total

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18)))
    print(solution.rangeSumBST(root, 7, 15))