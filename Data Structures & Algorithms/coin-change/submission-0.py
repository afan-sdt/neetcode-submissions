from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(amt):

            nonlocal res
            if amt == 0:
                return 0 # 0 coins needed
            if amt < 0:
                return float("inf") # invalid
            
            minimum = float("inf")
            for i in coins:
                minimum = min(minimum, 1 + dfs(amt-i))
            return minimum
        res = dfs(amount)
        return res if res != float("inf") else -1