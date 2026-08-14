class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = max(nums)
        curMax, curMin = 1, 1
        for n in nums:
            # if n == 0:
            #     curMin, curMax = 1, 1
            #     continue
            tmp = curMax
            curMax = max(curMax * n, n*curMin, n)
            curMin = min(tmp*n, n * curMin, n)
            res = max(res, curMax)
        return res   
        
        