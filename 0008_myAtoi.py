"""
8. String to Integer (atoi)

URL: https://leetcode.com/problems/string-to-integer-atoi/
Level: Medium
"""
import re

class Solution:
    def myAtoi(self, s: str) -> int:
        # """
        # 正規表現を使って数字のみ抽出する場合
        # """
        # if len(s) == 0:
        #     return 0

        # INT_MAX = 2**31 -1
        # INT_MIN = -2**31
        # pattern = r"^\s*([-|+]?[0-9]+)"
        # match = re.match(pattern, s)
        # if match is None:
        #     return 0

        # num = match.group(1)

        # if int(num) < INT_MIN:
        #     return INT_MIN
        # elif int(num) > INT_MAX:
        #     return INT_MAX
        # else:
        #     return int(num)

        """
        文字列の先頭から順番に処理。もし空白、+/-、数字以外があれば0を返す。
        オーバーフローチェックをして、超えたらINT_MIN/INT_MAXを返す。
        """
        INT_MAX = 2**31 -1
        INT_MIN = -2**31
        is_negative = False
        result = 0

        i = 0
        while i < len(s) and s[i] == ' ':
            i +=1

        if i < len(s) and s[i] == '-':
            i +=1
            is_negative = True
        elif i < len(s) and s[i] == '+':
            i +=1
        
        while i < len(s):
            if not s[i].isnumeric():
                break
            else:                    
                if result > INT_MAX//10:
                    return INT_MAX if not is_negative else INT_MIN
                    
                if result == INT_MAX//10:
                    if is_negative and int(s[i]) > 8:
                        return INT_MIN
                    if not is_negative and int(s[i]) > 7:
                        return INT_MAX

                result = result*10 + int(s[i])
            i += 1
        if is_negative:
            result *= -1
        
        return result

if __name__ == '__main__':
    solution = Solution()
    s = '       -2147483648'
#    s = "4193 with words"
#    s = '-91283472332'
    print(solution.myAtoi(s))