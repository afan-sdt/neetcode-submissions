class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        currSum = 0
        def dfs(i):
            # at each index we can choose to add it or not add it
            nonlocal currSum
            if i >= len(nums):
                return
            if currSum == target:
                res.append(path.copy())
                return
            if currSum > target:
                return
            
            path.append(nums[i])
            currSum+= nums[i]
            dfs(i)
            path.pop()
            currSum -= nums[i]
            dfs(i+1)
            
        dfs(0)
        return res

            
            