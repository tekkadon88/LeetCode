# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self, root):
        self.root = root

    def dumpList(self):
        current = self.root
        while current:
            print(current.val, end=' ')
            current = current.next
        print('')

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

if __name__ == '__main__':
    root = ListNode(4)
    root.next = ListNode(5)
    root.next.next = ListNode(1)
    root.next.next.next = ListNode(9)
    solution = Solution(root)
    solution.deleteNode(root.next)
    solution.dumpList()