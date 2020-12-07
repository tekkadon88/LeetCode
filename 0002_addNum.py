class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 返却用の連結リスト
        answer = ListNode()
        # 今みているノード
        current = answer
        # 桁上がり
        carry = 0

        while l1 or l2:
            # ノードがあればそのノードの値、なければ0を入れる
            l1_val = l1.val if l1 is not None else 0
            l2_val = l2.val if l2 is not None else 0

            # l1とl2と前の桁の桁上がりの値を足し合わせ
            num = l1_val + l2_val + carry

            # もし合算値が10以上の場合、桁上がりを1にする、9以下なら0
            if num > 9:
                carry = 1
            else:
                carry = 0

            # 足し算結果を値にもつノードを追加
            current.next = ListNode(num % 10)

            # 次のノードへ
            current = current.next

            # l1とl2もそれぞれ次のノードへ処理をうつす
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # すべてのノードの足し合わせの後に、桁上がりが残っていた場合、そのノードを最後に追加
        if carry > 0:
            current.next = ListNode(carry)

        return answer.next

if __name__ == '__main__':
    solution = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    ln = solution.addTwoNumbers(l1, l2)

    while ln:
        print(ln.val)
        ln = ln.next