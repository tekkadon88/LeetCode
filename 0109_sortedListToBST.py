"""
109. Convert Sorted List to Binary Search Tree

URL: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
Level: Easy
"""
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        """
        まずLinkedListをListへ変換する。配列からBSTの変更は
        「108. Convert Sorted Array to Binary Search Tree」
        と同じ。
        """
        def convert(head: ListNode) -> List[int]:
            ans = []
            curr = head
            while curr:
                ans.append(curr.val)
                curr = curr.next
            return ans
        
        def formBST(left, right):
            nonlocal nums

            if left > right:
                return None
            
            p = left + (right - left) //2

            root = TreeNode(nums[p])
            root.left = formBST(left, p-1)
            root.right = formBST(p+1, right)
            return root

        nums = convert(head)
        return formBST(0, len(nums) -1)

if __name__ == '__main__':
    solution = Solution()
    head = ListNode(-10)
    head.next = ListNode(-3)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(5)
    head.next.next.next.next = ListNode(9)
    node = solution.sortedListToBST(head)