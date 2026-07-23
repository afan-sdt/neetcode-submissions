class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        prefix = 1
        res = [0]*len(nums)
        for i,n in enumerate(nums):
            res[i] = prefix
            prefix *=n
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * postfix
            postfix = nums[i] * postfix
        return res
