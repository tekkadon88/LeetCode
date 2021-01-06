"""
359. Logger Rate Limiter

URL: https://leetcode.com/problems/logger-rate-limiter/
Level: Easy
"""
class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.logs = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message in self.logs:
            if self.logs[message] <= timestamp:
                self.logs[message] = timestamp + 10
                return True
            else:
                return False
        else:
            self.logs[message] = timestamp + 10
            return True

logger = Logger()
print(logger.shouldPrintMessage(1, "foo"))
print(logger.shouldPrintMessage(2, "bar"))
print(logger.shouldPrintMessage(3, "foo"))
print(logger.shouldPrintMessage(8, "bar"))
print(logger.shouldPrintMessage(10, "foo"))
print(logger.shouldPrintMessage(11, "foo"))
