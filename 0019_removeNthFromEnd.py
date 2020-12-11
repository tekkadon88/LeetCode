'''
19. Remove Nth Node From End of List

URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Level: Medium
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # ポインタを２つ用意
        left = head
        right = head

        # rightポインタをnだけ進める
        while n > 0:
            if right.next is None:
                return head.next
            right = right.next
            n -= 1

        # rightポインタが最後のノードにいくまでleftとrightどちらも１つずつ進める
        # rightポインタはleftよりn先にいるので終端に来た時にはleftはn-1のところにいる
        while right.next:
            left = left.next
            right = right.next

        # n-1のノードのnextを2つ先のノードへつけかえる
        left.next = left.next.next

        return head


if __name__ == '__main__':
    solution = Solution()
    current = root = ListNode()
    for i in range(1, 6):
        current.next = ListNode(i)
        current = current.next
    
    n = 2
    ln = solution.removeNthFromEnd(root.next, n)
    while ln:
        print(ln.val, end=' ')
        ln = ln.next
    print('')