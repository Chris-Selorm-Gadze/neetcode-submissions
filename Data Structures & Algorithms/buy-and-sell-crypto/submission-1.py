'''
return max profit 

profit must be positive. profit = selling price - buying price. 
so we buy on a day that is low. 

            l         r 
 prices = [10,1,5,6,7,1] = 10 -1 = -9 
 note r < len(prices)

 l = 0
 r = 1 

curr_profit = 0 
maxProfit  = 0 

note: if rp > 0. move r forward 
      else: set l = r since we found a cheaper price 

O(n) complexity. 
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = 1 
        max_profit = 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit > 0: 
                max_profit = max(max_profit, profit)

            else:
                l = r
            
            r += 1
        return max_profit 
        
                
