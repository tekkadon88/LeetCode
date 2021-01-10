"""
66. Plus One

URL: https://leetcode.com/problems/plus-one/
Level: Easy
"""
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1

        while i >= 0:
            if digits[i] + carry > 9:
                digits[i] = 0
                carry = 1
            else:
                digits[i] = digits[i] + carry
                carry = 0
            i -= 1

        if carry == 1:
            return [1] + digits
        else:
            return digits

if __name__ == '__main__':
    solution = Solution()
    digits = [1,2,3]
    print(solution.plusOne(digits))