"""
5. Longest Palindromic Substring

URL: https://leetcode.com/problems/longest-palindromic-substring/
Level: Medium
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # """
        # Brute-force
        # """
        # if len(s) <=2:
        #     if s == s[::-1]:
        #         return s
        #     else:
        #         return s[0]

        # max_substr = s[0]
        # for i in range(len(s)):
        #     for j in range(len(s)-1, i, -1):
        #         if s[i] == s[j]:
        #             if s[i:j+1] == s[i:j+1][::-1]:
        #                 if len(max_substr) < len(s[i:j+1]):
        #                     max_substr = s[i:j+1]

        # return max_substr

        """
        Dynamic Programming

        例えば入力文字列が"abcba" (s='abcba') の場合で考える。DPテーブルは以下。

          a b c b a
        a T F F F T
        b   T F T F
        c     T F F
        b       T F
        a         T

        ここで dp[i][j]は入力文字列のインデックス。i=2, j=3なら s[2:4] = 'cb'
        対角(dp[i][j] i=j)は１文字だけを表すので必ずTrue。例えばdp[2][2] = 'c'
        対角の下側はみなくてよい。dp[3][0]とdp[0][3]の結果は同じ。
        
        処理は文字列の後ろから(DPテーブルの右下から)順番に見ていく。
        もしs[i] == s[j]となった場合、dp[i+1][j-1]がTrueであるならdp[i][j]もTrue
        """
        if len(s) <=2:
            if s == s[::-1]:
                return s
            else:
                return s[0]

        # DPテーブルの初期化
        dp = [ [False]*len(s) for _ in range(len(s)) ]
        ans = s[0]

        # dp[i][i]は入力文字列sのインデックスiの１文字を表す
        # 1文字だけの場合PalindromeになっているのでTrueをセット
        for i in range(len(s)):
            dp[i][i] = True

        # 文字列の後ろからみていく
        for j in range(len(s)-1, -1, -1):
            for k in range(j+1, len(s)):
                if s[j] == s[k]:
                    # 連続する２文字が同じである場合か、s[j+1:k]がPalindromeならs[j:k+1]もPalindrome
                    if k - j == 1 or dp[j+1][k-1] == True:
                        dp[j][k] = True

                        if len(ans) < len(s[j:k+1]):
                            ans = s[j:k+1]
        
        # print(dp)
        return ans

if __name__ == '__main__':
    solution = Solution()
    #s = 'ababa'
    #s = 'abcba'
    #s = 'abaca'
    s = 'abcda'
    print(solution.longestPalindrome(s))