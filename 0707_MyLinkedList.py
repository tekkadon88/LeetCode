"""
707. Design Linked List

URL: https://leetcode.com/problems/design-linked-list/
Level: Medium
"""
class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.head = Node()
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.size:
            return -1
        
        current = self.head

        for i in range(index + 1):
            current = current.next
        
        return current.value
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return 
        
        # According to the constraints, index is 0 <= index <= 1000, so it should be non-negative 

        prev = self.head
        for i in range(index):
            prev = prev.next
        
        new_node = Node(val)
        next_node = prev.next
        prev.next = new_node
        new_node.next = next_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.size:
            return
        
        prev = self.head
        for i in range(index):
            prev = prev.next

        prev.next = prev.next.next

        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1,2)
print(obj.get(1))
obj.deleteAtIndex(1)
print(obj.get(1))