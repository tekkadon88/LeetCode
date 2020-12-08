# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 今見てるノード
        current = head
        
        # 1つ前のノード
        prev = None

        while current:
            # 次のノードをnextNodeで保持
            nextNode = current.next
            # 現在のノードのnextポインタを1つ前のノードへつけかえる
            current.next = prev
            # 現在見てるノードを1つ前のノードとして
            prev = current
            # 次のノードへ処理をうつす
            current = nextNode

        return prev

if __name__ == '__main__':
    solution = Solution()
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(4)
    root.next.next.next.next = ListNode(5)
    node = solution.reverseList(root)

    while node:
        print(node.val,end='->')
        node = node.next
    print('NULL')