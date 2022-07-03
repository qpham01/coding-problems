# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in 
# the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self, prices:list):
        days = len(prices)
        previousMaxPrice = 0
        maxProfit = 0
        for i in range(days - 1, -1, -1):
            if prices[i] > previousMaxPrice:
                previousMaxPrice = prices[i]
            priceDiff = previousMaxPrice - prices[i]
            if priceDiff > maxProfit:
                maxProfit = priceDiff
                
        print("max profit:", maxProfit)                
        return maxProfit
    
            
solution = Solution()

answer = solution.maxProfit([7,1,5,3,6,4])
assert answer == 5

answer = solution.maxProfit([7,6,4,3,1])
assert answer == 0

answer = solution.maxProfit([7,6,4,3,1,2])
assert answer == 1

answer = solution.maxProfit([3,2,6,5,0,3])
assert answer == 4
