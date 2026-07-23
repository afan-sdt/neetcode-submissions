class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # thought process: choose one element, add it to result
        # take the rest of that result and pass it as remaining
        # if remaining is empty, you have a result

        res = []
        curr = []

        def backtrack(remaining: List[int]):
            nonlocal curr
            if len(remaining) == 0:
                res.append(curr[:])
            for i in range(len(remaining)):
                curr.append(remaining[i])
                backtrack(remaining[:i] + remaining[i+1:])
                curr.pop()
        backtrack(nums)
        return res























        # res = []
        # sol = []

        # def backtrack():
        #     if len(sol) == len(nums):
        #         res.append(sol[:]) #returns copy
        #         return
            
        #     for i in nums:
        #         if i not in sol:
        #             sol.append(i)
        #             backtrack()
        #             sol.pop()
        # backtrack()
        # return res