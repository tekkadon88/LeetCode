class Solution:
    def twoSum(self, nums, target):
        '''
          hashmapを使ったバージョン
        '''
        # 入力配列の長さ
        length = len(nums)

        # {value: index} のマッピングテーブルを作成
        table = dict()
        for i, v in enumerate(nums):
            table[v] = i
        
        for j in range(length):
            # 探している値がテーブルにあるかをチェック
            if target - nums[j] in table and j != table[target - nums[j]]:
                return [j, table[target - nums[j]]]

if __name__ == '__main__':
    solution = Solution()
    nums = [2,7,11,15]
    target = 9
    print(solution.twoSum(nums, target))