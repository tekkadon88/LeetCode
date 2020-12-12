"""
101. Symmetric Tree

URL: https://leetcode.com/problems/symmetric-tree/
Level: Easy
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        '''
        基本的なアプローチは"100. Same Tree"と同じ
        対称チェックなので比較を対称にやるだけ
        '''
        def check(t1, t2):
            if t1 is None and t2 is None:
                return True
            if t1 is None or t2 is None:
                return False
            if t1.val != t2.val:
                return False

            return check(t1.left, t2.right) and check(t1.right, t2.left)
        
        if root is None:
            return True

        return check(root.left, root.right)

if __name__ == '__main__':
    solution = Solution()
    t1 = TreeNode(1, TreeNode(2), TreeNode(2))
    print(solution.isSymmetric(t1))

    t2 = TreeNode(1, None, TreeNode(2))
    print(solution.isSymmetric(t2))