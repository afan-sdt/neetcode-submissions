class Solution:
    def jump(self, nums: List[int]) -> int:
        L, R = 0, 0
        if len(nums) == 1:
            return 0
        jumps = 0
        while R < len(nums) - 1:
            # we iterate from L to R, increasing nextR to max possible reachable at this jump
            nextR = -1
            while L <= R:
                nextR = max(L+nums[L], nextR)
                L+=1
            R = nextR
            jumps += 1
        return jumps


        