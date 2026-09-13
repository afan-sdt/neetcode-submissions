class Solution:
    def findMin(self, nums: List[int]) -> int:
        # the minimum is the only number where the number before it is greater
        # we can decide to go left or go based on if the entire sequence 
        # one side is sorted, go other way
        # both sides are sorted, the minimum is the left pointer
        # both sides are sorted if the left pointer is less than mid and right pointer is more than mid
        

        #behavior: compare with left, if left is greater, pivot is on this side
        # if right is less, pivot is on this side
        # if neither, pivot is the left pointer

        l, r = 0, len(nums)-1

        while l <= r:
            mid = l + ((r-l)//2)
            if mid > 0 and nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[l] > nums[mid]:
                r = mid - 1
            elif nums[r] < nums[mid]:
                l = mid + 1
            else:
                return nums[l]
        return r