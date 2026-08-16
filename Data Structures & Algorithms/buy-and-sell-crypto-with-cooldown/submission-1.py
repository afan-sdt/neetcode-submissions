class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        
        def dfs(purchaseTime, currTime):
            if (purchaseTime, currTime) in memo:
                return memo[(purchaseTime, currTime)]
            if currTime >= len(prices):
                return 0
            transact = 0
            if purchaseTime == -1: #no coin held, purchase
                transact = dfs(currTime, currTime + 1)
            else:
                transact = prices[currTime] - prices[purchaseTime] + dfs(-1, currTime + 2)
            memo[(purchaseTime, currTime)] = max(transact, dfs(purchaseTime, currTime + 1))
            return memo[(purchaseTime, currTime)]
        return dfs(-1, 0)
            
            
        