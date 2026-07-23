class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # define a recursive function where you loop through until
        # 
        res = []

        def dfs(i: int, curr: List[int], total: int):
            if i >= len(nums) or total > target:
                return
            if total == target:
                res.append(curr.copy())
                return
            #add this one to output
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            #exclude this one from output
            curr.pop()
            dfs(i+1, curr, total)
        
        dfs(0, [], 0)

        return res

        # res = set()
        # def validPath(sumSoFar: int, elementsSoFar: List[int]) -> None:
        #     nonlocal res
        #     if sumSoFar == target:
        #         elementsSoFar.sort()
        #         res.add(tuple(elementsSoFar))
        #         print(elementsSoFar)
        #         return
        #     if sumSoFar > target:
        #         return
        #     for x in nums:
        #         validPath(sumSoFar + x, elementsSoFar + [x])

        # for x in nums:
        #     validPath(x, [x])
        # return [list(x) for x in res]