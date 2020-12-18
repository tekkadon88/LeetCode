"""
20. Valid Parentheses

URL: https://leetcode.com/problems/valid-parentheses/
Level: Easy
"""
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        stack = list()
        close_parentheses = {')':'(', ']':'[', '}':'{'}

        # 先頭から順番に処理。もし開き括弧ならスタックに追加。
        # 閉じ括弧の場合、スタックの一番上が同じ種類の開き括弧かチェックして、
        # もし同じであれば処理継続。違えばきちんと括弧が閉じていないのでFalse
        for p in s:
            print(p)
            if p == '(' or p == '[' or p == '{':
                stack.append(p)
                continue
            if p in close_parentheses:
                if stack and stack.pop() == close_parentheses[p]:
                    continue
                else:
                    return False
        
        if len(stack) >0:
            return False

        return True

if __name__ == '__main__':
    solution = Solution()
    s = '()[{}]'
    print(solution.isValid(s))