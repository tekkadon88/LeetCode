"""
100. Same Tree

URL: https://leetcode.com/problems/same-tree/
Level: Easy
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        '''
        両方の二分探索木を同じようにみていって比較する
        '''
        def dfs(t1, t2):
            if t1 is None and t2 is None:
                return True
            
            if t1 is None or t2 is None:
                return False
            
            if t1.val != t2.val:
                return False
            
            return dfs(t1.left, t2.left) and dfs(t1.right, t2.right)
        
        return dfs(p, q)
            
if __name__ == '__main__':
    solution = Solution()
    root1 = TreeNode(1, TreeNode(2), TreeNode(3))
    root2 = TreeNode(1, TreeNode(2), TreeNode(3))

    #root1 = TreeNode(1, None, TreeNode(2))
    #root2 = TreeNode(1, TreeNode(2), None)

    print(solution.isSameTree(root1, root2))