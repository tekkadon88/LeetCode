'''
160. Intersection of Two Linked Lists

URL: https://leetcode.com/problems/intersection-of-two-linked-lists/
Level: Easy

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None
        
        curr1 = headA
        curr2 = headB
        
        '''
          curr1がheadAの最後まで行ったら、headBの先頭へ移動してheadBの最後まで調べる
          同様にcurr2がheadBの最後までいったら、headAの先頭へ移動してheadAの最後まで調べる
          こうすることによりどちらも同じ距離だけ走査することになり、もし交差点があれば必ず同時に同じノードに到達する

          例えば
          headA: 1->2->3->4->5, headB: 6->3->4->5 (3が交差点) となっていた場合、
          curr1は 1->2->3->4->5->6->3->4->5
          curr2は 6->3->4->5->1->2->3->4->5
          とみていくことになり、同時に交差点である3のノードに到達する
          もし交差点がない場合は、同時にtail (= None)となりループが終了する
        '''
        while curr1 != curr2:
            if curr1 == None:
                curr1 = headB
            else:
                curr1 = curr1.next
                
            if curr2 == None:
                curr2 = headA
            else:
                curr2 = curr2.next
        
        print(curr1, curr2)
        return curr1

if __name__ == '__main__':
    solution = Solution()
    rootA = ListNode(1)
    rootA.next = ListNode(2)
    rootB = ListNode(6)
    rootB.next = ListNode(7)

    tmp = ListNode(3)
    tmp.next = ListNode(4)
    tmp.next.next = ListNode(5)

    rootA.next.next = tmp
    rootB.next.next = tmp

    ln = solution.getIntersectionNode(rootA, rootB)

    while ln:
        print(ln.val, end=' ')
        ln = ln.next
    print('')