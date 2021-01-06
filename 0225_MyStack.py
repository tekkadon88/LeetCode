""" 
225. Implement Stack using Queues

URL: https://leetcode.com/problems/implement-stack-using-queues/
Level: Easy
"""
from queue import Queue
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = Queue()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.put(x)
        for _ in range(self.queue.qsize()-1):
            tmp = self.queue.get()
            self.queue.put(tmp)        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.get()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        top_element = self.queue.get()
        self.queue.put(top_element)
        for _ in range(self.queue.qsize()-1):
            tmp = self.queue.get()
            self.queue.put(tmp)
        return top_element

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.queue.empty():
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.top())
print(obj.pop())
print(obj.empty())