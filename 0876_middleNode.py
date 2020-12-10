'''
876. Middle of the Linked List

URL: https://leetcode.com/problems/middle-of-the-linked-list/
Level: Easy

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        current = head
        length = 0

        # リストの長さをチェック
        while current:
            length += 1
            current = current.next

        length = length // 2
        node = head

        # 真ん中のノードまでみていき、目的のノードにたどりついたらそれを返す
        while length > 0:
            node = node.next
            length -= 1
        
        return node

if __name__ == '__main__':
    solution = Solution()
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(4)
    root.next.next.next.next = ListNode(5)

    ln = solution.middleNode(root)

    while ln:
        print(ln.val, end=' ')
        ln = ln.next
    print('')