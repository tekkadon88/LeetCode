# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        arr = list()

        while head:
            arr.append(head.val)
            head = head.next
        
        return arr == arr[::-1]

if __name__ == '__main__':
    solution = Solution()
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(2)
    print(solution.isPalindrome(root))