class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #since each element can reach your max, at each step you take the element with the farthest reach
        L, R = 0, 0
        while L <= R and R < (len(nums)-1):
            print(L, R)
            R = max(L+nums[L], R)
            L+=1
        if R >= (len(nums) - 1):
            return True
        return False
