class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #initialize to 0 can't be less than 0
        maxProfit = 0
        l, r = 0, 0
        while r < len(prices):
            diff = prices[r] - prices[l]
            if diff < 0:
                #negative, move l here b/c new low
                l = r
            else:
                maxProfit = max(maxProfit, diff)
            r+=1
        return maxProfit