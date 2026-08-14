class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False
        halfSum = totalSum//2


        def dfs(sumSoFar, rest):
            if sumSoFar == halfSum and len(rest) != []:
                return True
            if sumSoFar > totalSum:
                return False
            
            for i in range(len(rest)):
                if dfs(sumSoFar + rest[i], rest[:i] + rest[i+1:]):
                    return True
            return False
        return dfs(0, nums)

        