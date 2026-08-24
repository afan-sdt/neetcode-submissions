class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) in (0,1):
            return len(nums)
        nums.sort()
        curr = 1
        res = 1

        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            if nums[i+1] == (nums[i]+1):

                curr += 1
                res = max(res, curr)
            else:

                curr = 1
        return res
        
            