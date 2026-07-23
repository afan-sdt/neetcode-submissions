class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #first solution: sort and then return the kth solution
        nums.sort()
        return nums[-k]