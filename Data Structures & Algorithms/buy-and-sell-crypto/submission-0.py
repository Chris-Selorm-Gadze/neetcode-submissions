class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l,r = 0, 1 # left = buy, right = sell 

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)
            else:
                l = r
            r += 1
        return maxP
