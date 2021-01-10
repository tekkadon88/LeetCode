"""
67. Add Binary

URL: https://leetcode.com/problems/add-binary/
Level: Easy
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) -1
        j = len(b) -1
        carry = 0
        ans = []

        while i >= 0 or j >= 0:
            val_a = int(a[i]) if i >= 0 else 0
            val_b = int(b[j]) if j >= 0 else 0

            if val_a + val_b + carry >= 2:
                ans.append(val_a + val_b + carry - 2)
                carry = 1
            else:
                ans.append(val_a + val_b + carry)
                carry = 0
            
            i -=1
            j -=1
        if carry:
            ans.append(carry)

        return ''.join( str(x) for x in ans[::-1] )

if __name__ == '__main__':
    solution = Solution()
    a = '1010'
    b = '1101'
    print(solution.addBinary(a, b))