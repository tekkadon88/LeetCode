"""
121. Best Time to Buy and Sell Stock

URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Level: Easy
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Brute Force (Time Limit Exceeded)
        length = len(prices)
        if length == 0 or length == 1:
            return 0

        profit = 0
        for i in range(length):
            for j in range(i+1, length):
                if prices[j] - prices[i] > 0:
                    profit = max(profit, prices[j]-prices[i])
        
        return profit
        '''
        
        min_price = float('inf')
        profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
        
            if price - min_price > profit:
                profit = price - min_price
        
        # print(profit)
        return profit

if __name__ == '__main__':
    solution = Solution()
    prices = [7,1,5,3,6,4]
    print(solution.maxProfit(prices))

    prices = [7,6,4,3,1]
    print(solution.maxProfit(prices))