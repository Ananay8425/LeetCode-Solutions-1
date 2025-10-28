# Best time to buy and sell stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = prices[0]
        profit = 0
        for i in range(len(prices)):
            if(prices[i] < b):
                b = prices[i]
            elif(prices[i] - b > profit):
                profit = prices[i] - b
        return profit