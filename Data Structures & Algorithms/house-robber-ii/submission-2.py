class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.help(nums[:-1]) , self.help(nums[1:]))
    
    def help(self, arr):
        memo = {}
        n = len(arr)
        def dfs(index):
            if index >= n:
                return 0
            if index in memo:
                return memo[index]
            res = max(arr[index] + dfs(index+2), dfs(index+1))
            memo[index] = res
            return res
        return dfs(0)
