class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        rolling = 1
        for i in range(len(nums)):
            res[i] = rolling
            rolling = rolling * nums[i]
        rolling = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = rolling * res[i]
            rolling = rolling * nums[i]
        return res
            
            
