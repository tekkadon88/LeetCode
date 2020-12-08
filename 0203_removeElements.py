# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # ダミーヘッド
        dummy = ListNode()
        dummy.next = head

        # prevをダミーヘッド、currentをリストの最初のノードで初期化
        prev = dummy
        current = head

        # 入力リストのノードがなくなるまでチェック
        while current:
            # もし現在のノードの値が探している値と一致したら、
            # 1つ前のノードのnextとポインタを現在のノードの次のノードへつけかえる
            # これによって現在見ているノード (current) をスキップする
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        
        return dummy.next

if __name__ == '__main__':
    input_array = [1,2,6,3,4,5,6]
    head = ListNode()
    current = head

    for i in input_array:
        current.next = ListNode(i)
        current = current.next

    solution = Solution()
    val = 6
    ln = solution.removeElements(head.next, val)

    while ln:
        print(ln.val, end=' ')
        ln = ln.next
    print('')