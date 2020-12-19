"""
13. Roman to Integer

URL: 
Level: Easy
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        # ローマ数字からの変換テーブル
        mapping = {
            'I':1, 'IV':4,'V': 5, 'IX':9, 'X':10,
            'XL':40, 'L':50, 'XC':90, 'C':100,
            'CD':400, 'D':500, 'CM':900, 'M':1000
        }

        ans = 0
        i = 0

        while i < len(s):
            # 連続2文字がmappingテーブルにあればその値を加算して2つ進める
            # それ以外は1文字のみのマッチなのでそのまま加算
            if i <= len(s) -2 and s[i:i+2] in mapping:
                ans += mapping[s[i:i+2]]
                i +=2
            else:
                ans += mapping[s[i]]
                i +=1
        # print(ans)
        return ans

if __name__ == '__main__':
    solution = Solution()
    s = 'XII'
    s = 'III'
    s = 'IV'
    s = 'IX'
    s = 'LVIII'
    s = 'MCMXCIV'
    print(solution.romanToInt(s))