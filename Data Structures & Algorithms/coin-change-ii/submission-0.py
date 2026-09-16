class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(i, amt):
            if (i, amt) in memo:
                return memo[(i, amt)]
            if amt == amount:
                return 1
            if amt > amount:
                return 0
            total = 0
            for j in range(i, len(coins)):
                total += dfs(j, amt + coins[j])
            memo[(i,amt)] = total
            return total
        return dfs(0, 0)