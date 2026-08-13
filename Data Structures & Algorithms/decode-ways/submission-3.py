class Solution:
    def numDecodings(self, s: str) -> int:

        memo = {}


        def dfs(index):
            if index == len(s):
                return 1
            if index > len(s):
                return 0
            if index in memo:
                return memo[index]
            totalWays = 0
            if int(s[index:index+1]) >= 1 and int(s[index:index+1]) <=9:
                totalWays += dfs(index+1)
            if int(s[index:index+2]) >= 10 and int(s[index:index+2]) <= 26:
                totalWays+= dfs(index+2)
            memo[index] = totalWays
            return totalWays

        return dfs(0)
        
