'''
141. Linked List Cycle

URL: https://leetcode.com/problems/linked-list-cycle/
Level: Easy
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 空のリストの場合はFalse
        if head is None:
            return False

        # slowとfastの2つのポインタを用意
        # slowは１つずつ、fastは2つずつ進む
        # もし循環していればいつかは同じノードで出会う
        # 循環していなければfastポインタがリストの終端に到達して終了
        slow = head
        fast = head.next

        while slow != fast:
            if fast is None or fast.next is None:
                return False

            slow = slow.next
            fast = fast.next.next
        
        return True

if __name__ == '__main__':
    solution = Solution()
    root = ListNode(3)
    conn = ListNode(2)
    root.next = conn
    root.next.next = ListNode(0)
    root.next.next.next = ListNode(4)
    root.next.next.next.next = conn

    print(solution.hasCycle(root))