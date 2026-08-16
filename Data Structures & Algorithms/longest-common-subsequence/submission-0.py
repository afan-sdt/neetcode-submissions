class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def dfs(ind1, ind2):
            if (ind1, ind2) in memo:
                return memo[(ind1, ind2)]
            if ind1 == len(text1) or ind2 == len(text2):
                # one has reached the end, therefore can be no LCS
                return 0
            if text1[ind1] == text2[ind2]:
                memo[(ind1, ind2)] = 1 + dfs(ind1+1, ind2+1)
            else:
                memo[(ind1, ind2)] = max(dfs(ind1+1, ind2), dfs(ind1, ind2+1))
            return memo[(ind1, ind2)]
        return dfs(0,0)
            