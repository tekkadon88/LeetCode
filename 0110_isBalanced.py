# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(node):
            if node is None:
                return (True, 0)
            
            left_is_balanced, left_height = helper(node.left)
            right_is_balanced, right_height = helper(node.right)
            # print(node.val, left_height, right_height)

            if not left_is_balanced:
                return (False, 0)
            if not right_is_balanced:
                return (False, 0)
            
            return (abs(left_height - right_height) <= 1, 1+max(left_height, right_height))
        
        return helper(root)[0]

if __name__ == '__main__':
    solution = Solution()
    #root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(5)), TreeNode(6)), TreeNode(10))
    print(solution.isBalanced(root))