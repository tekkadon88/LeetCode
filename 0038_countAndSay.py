"""
38. Count and Say

URL: https://leetcode.com/problems/count-and-say/
Level: Easy
"""
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'

        num_string = self.countAndSay(n-1)
        curr_char = num_string[0]
        count = 1
        ans = list()

        for i in range(1, len(num_string)):
            if num_string[i] == curr_char:
                count +=1
            else:
                ans.append((str(count), curr_char))
                curr_char = num_string[i]
                count = 1

        if curr_char == num_string[-1]:
            ans.append((str(count), curr_char))

        #val = ''.join(i+j for i, j in ans)
        # print(val)

        return ''.join(i+j for i, j in ans)

if __name__ == '__main__':
    solution = Solution()
    n = 5
    print(solution.countAndSay(n))