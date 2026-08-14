class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            # maxLISprev = 1
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i] and dp[j] >= dp[i]:
                    dp[i] = dp[j] + 1
        print(dp)
        return max(dp)

        
                



        