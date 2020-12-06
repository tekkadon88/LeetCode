class Solution:
    def twoSum(self, nums, target):
        # 入力配列の長さ
        length = len(nums)

        for i in range(length):
            for j in range(i+1, length):
                # nums[i]とnums[j]の合計がtargetに等しいペアが見つかったら終了
                if nums[j] == target - nums[i]:
                    return [i, j]

if __name__ == '__main__':
    solution = Solution()
    nums = [2,7,11,15]
    target = 9
    print(solution.twoSum(nums, target))