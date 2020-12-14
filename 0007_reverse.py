"""
7. Reverse Integer

URL: https://leetcode.com/problems/reverse-integer/
Level: Easy
"""
class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX=2**31-1  # INT_MAX =  2147483647
        INT_MIN=-2**31   # INT_MIN = -2147483648
        is_negative = False
        ans = 0

        if -9 <= x <= 9:
            return x

        if x < 0:
            is_negative = True
            x = abs(x)

        while x != 0:
            x, r = divmod(x, 10)

            if is_negative:
                if ans > (INT_MAX+1) // 10 or (ans == (INT_MAX+1)//10 and r > 8):
                    return 0
            else:
                if ans > INT_MAX // 10 or (ans == INT_MAX // 10 and r > 7):
                    return 0
        
            ans = ans*10 + r
        
        if is_negative:
            ans *= -1
        
        return ans

if __name__ == "__main__":
    solution = Solution()
    x = 123
    print(solution.reverse(x))