class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # define a recursive function where you loop through until
        # 
        res = set()
        def validPath(sumSoFar: int, elementsSoFar: List[int]) -> None:
            nonlocal res
            if sumSoFar == target:
                elementsSoFar.sort()
                res.add(tuple(elementsSoFar))
                print(elementsSoFar)
                return
            if sumSoFar > target:
                return
            for x in nums:
                validPath(sumSoFar + x, elementsSoFar + [x])

        for x in nums:
            validPath(x, [x])
        return [list(x) for x in res]