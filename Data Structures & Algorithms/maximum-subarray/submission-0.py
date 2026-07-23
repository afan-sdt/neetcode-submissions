class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        for i in nums:
            curSum = max(curSum, 0) + i
            maxSum = max(curSum, maxSum)
        return maxSum