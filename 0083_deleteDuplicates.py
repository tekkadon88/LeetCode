'''
83. Remove Duplicates from Sorted List

URL: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
Level: Easy
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        
        return head


if __name__ == '__main__':
    solution = Solution()
    root = ListNode(1)
    root.next = ListNode(1)
    root.next.next = ListNode(1)
    root.next.next.next = ListNode(2)
    root.next.next.next.next = ListNode(3)
    root.next.next.next.next.next = ListNode(3)

    ln = solution.deleteDuplicates(root)

    while ln:
        print(ln.val, end=' ')
        ln = ln.next
    print('')