"""
346. Moving Average from Data Stream

URL: https://leetcode.com/problems/moving-average-from-data-stream/
Level: Easy
"""
from queue import Queue
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = Queue(size)
        self.window_total = 0
        

    def next(self, val: int) -> float:

        if self.queue.full():
            top = self.queue.get()
            self.queue.put(val)
            self.window_total = self.window_total - top + val
        else:
            self.queue.put(val)
            self.window_total += val
        
        return self.window_total / self.queue.qsize()
        


# Your MovingAverage object will be instantiated and called as such:
obj = MovingAverage(3)
print(obj.next(1))
print(obj.next(10))
print(obj.next(3))
print(obj.next(5))