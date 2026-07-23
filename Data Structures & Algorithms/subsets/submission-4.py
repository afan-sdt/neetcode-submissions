class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def solve(subset: List[int], rem: List[int]) -> None:
            print(subset)
            if len(rem) == 0:
                result.append(subset)
                return
            solve(subset + [rem[0]], rem[1:])
            solve(subset, rem[1:])
        solve([],nums)
        return result

        