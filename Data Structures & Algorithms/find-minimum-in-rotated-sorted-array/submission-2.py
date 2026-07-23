class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1

        while l<=r:
            middle = (l+r)//2
            
            if nums[(middle-1)%len(nums)] > nums[middle] and nums[(middle+1)%len(nums)] > nums[middle]:
                return nums[middle]
            if nums[l] > nums[middle]:
                r = middle-1
            elif nums[r] < nums[middle]:
                l = middle + 1
            else:
                return nums[l]
            
        return 0