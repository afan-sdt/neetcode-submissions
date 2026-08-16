class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #we want to contain two pointers which represent the window we're considering
        # we keep track of maxSum so far
        # we keep adding to our subarray until it becomes negative. At that point,we reset the subarray to i+1 and our cursum
        maxSum = float("-inf")
        curSum = 0
        l = 0
        for n in nums:
            curSum += n
            maxSum = max(curSum, maxSum)
            if curSum < 0:
                curSum = 0
        return maxSum
