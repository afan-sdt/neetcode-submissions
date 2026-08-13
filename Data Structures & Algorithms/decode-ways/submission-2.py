class Solution:
    def numDecodings(self, s: str) -> int:

        memo = {}


        def dfs(sub):
            if sub == "":
                return 1
            if sub in memo:
                return memo[sub]
            totalWays = 0
            if int(sub[:1]) >= 1 and int(sub[:1]) <=9:
                totalWays += dfs(sub[1:])
            if int(sub[:2]) >= 10 and int(sub[:2]) <= 26:
                totalWays+= dfs(sub[2:])
            memo[sub] = totalWays
            return totalWays

        return dfs(s)
        
