class Solution:
    def rob(self, nums: List[int]) -> int:
        # at each step, you make a decision: rob this house or not
        # you want to maximize the amount you make at the end
        # the maximum you can rob at any house is either
        # dp[i-2] + cost[i] or dp[i-1]. that would be the "maxSoFar"
        # dp[0] = nums[0] assume array ends at 1, max is this
        # dp[1] = max(nums[1] or nums[0]) the max this one makes is whatever is 
        n = len(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        if n == 1:
            return nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return max(dp[n-1], dp[n-2])
