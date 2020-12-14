"""
9. Palindrome Number

URL: https://leetcode.com/problems/palindrome-number/
Level: Easy
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        # strに変換して、反転文字列と同じかチェック
        return str(x) == str(x)[::-1]
        '''

        # Follow upで文字列変換しないで解けとあるので文字列変換しない場合の解法
        
        # negative numberならFalseを返す
        if x < 0:
            return False

        reversed = 0
        tmp = x

        # 反転させてもとのxと比較する。同じならTrue、違えばFalseが返る
        while tmp > 0:
            tmp, r = divmod(tmp, 10)
            reversed = reversed * 10 + r
        
        # print(f'x: {x}, reversed_x: {reversed}')
        return x == reversed


if __name__ == '__main__':
    solution = Solution()
    x = 1221
    print(solution.isPalindrome(x))

    x = 12321
    print(solution.isPalindrome(x))

    x = 122321
    print(solution.isPalindrome(x))