"""
6. ZigZag Conversion

URL: https://leetcode.com/problems/zigzag-conversion/
Level: Medium
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans = [[] for _ in range(numRows) ]

        row = 0
        direction = 1
        for i in range(len(s)):
            ans[row].append(s[i])
            if row == numRows -1 and direction == 1:
                direction = -1
            if row == 0 and direction == -1:
                direction = 1

            row += direction

        return ''.join(''.join(c) for c in ans)

if __name__ == '__main__':
    solution = Solution()
    s = 'PAYPALISHIRING'
    numRows = 3
    s = 'AB'
    numRows = 1
    print(solution.convert(s, numRows))