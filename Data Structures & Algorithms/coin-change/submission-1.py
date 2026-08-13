
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = { 0: 0}
        def dfs(amt):
            if amt in memo: 
                return memo[amt]
            nonlocal res
            if amt < 0:
                return float("inf") # invalid
            
            minimum = float("inf")
            for i in coins:
                minimum = min(minimum, 1 + dfs(amt-i))
            memo[amt] = minimum
            return minimum
        res = dfs(amount)
        return res if res != float("inf") else -1