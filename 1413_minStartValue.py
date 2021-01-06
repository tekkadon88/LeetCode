"""
1413. Minimum Value to Get Positive Step by Step Sum

URL: https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
Level: Easy
"""
from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = 0
        minimum = float('inf')

        # 配列の要素を１つずつみていき、取りうる最小の値を探す
        for num in nums:
            prefix_sum += num
            minimum = min(prefix_sum, minimum)
            # print(prefix_sum, minimum)

        # 最小値が負の数だった場合、足して1になる数が答えとなる。
        # 例えば最小値が−10だったら11を返す。
        # もし最小値が正の数だったら1を返す。
        return max(1-minimum, 1)

if __name__ == '__main__':
    solution = Solution()
    nums = [-3,2,-3,4,2]
    nums = [1,2]
    print(solution.minStartValue(nums))