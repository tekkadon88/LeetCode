"""
26. Remove Duplicates from Sorted Array

URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Level: Easy
"""
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        nums = [1,1,2,2,2,3,4,5,5,6]
        
        set()を使えれば１行で終わりそうな問題だけど、in-placeでとあるので
        リストの先頭から重複を確認しながら見ていき、
        重複があれば次の重複していない値までスキップ

        ２つポインタを用意(slowとfast)。fastは重複があれば先に進めて
        違う値になったらslowと値を交換。
        上の例でいくと、slowはインデックス0、fastはインデックス1から始める。
        nums[0]とnums[1]はともに1なので、fastポインタを次に進める。
        nums[2]は2なので、slowポインタを1つ進めてnums[1]とnums[2]を交換。
        順々に繰り返してfastポインタがリストの最後になるまで続ける。
        終了時のslowポインタが重複なしのリストの最後のインデックスなので長さはslow+1
        """
        slow = 0
        fast = 1

        while fast < len(nums):
            if nums[fast] == nums[slow]:
                fast +=1
            else:
                slow +=1
                nums[slow] = nums[fast]
            
            #print(nums)
        
        # del(nums[slow+1:])
        # print(nums)
        return slow+1



if __name__ == '__main__':
    solution = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(solution.removeDuplicates(nums))