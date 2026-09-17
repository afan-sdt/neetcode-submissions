class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #CARIT
        # clarify: are there repeats? can each number be only used once? does each number have to be used or can you skip?
        # Approach: we try each combination. we generate all possible combinations using dfs
        # we use the totalsoFar and the currentIndex as the input into our dfs function
        # 
        memo = {}
        def dfs(sumSoFar, index):
            if (sumSoFar, index) in memo:
                return memo[(sumSoFar, index)]
            if index == len(nums):
                if sumSoFar == target:
                    return 1
                else:
                    return 0
            memo[(sumSoFar,index)] = dfs(sumSoFar + nums[index], index + 1) + dfs(sumSoFar - nums[index], index + 1)
            return memo[(sumSoFar, index)]
        return dfs(0,0)