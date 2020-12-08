# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        current = head

        # l1かl2のどちらかがtailになるまでみていく
        while l1 and l2:
            # もしl1の値がl2より大きい場合、現在のl2ノードをつなげて次のl2ノードへ
            if l1.val >= l2.val:
                current.next = l2
                l2 = l2.next
            else: # もしl2の方が大きい場合はl1ノードをつなげて次のl1ノードへ
                current.next = l1
                l1 = l1.next
            current = current.next

        # l1かl2のノードの残りをつなげる
        current.next = l1 or l2
        
        # headはダミーなので、次のノードを返却
        return head.next

if __name__ == '__main__':
    solution = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(5)
    ln = solution.mergeTwoLists(l1, l2)

    while ln:
        print(ln.val, end=" ")
        ln = ln.next
    print('')