class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        def solve(index) -> None:
            if index == len(nums):
                result.append(subset[:])
                return
            subset.append(nums[index])
            solve(index+1)
            subset.pop()
            solve(index +1)
        solve(0)
        return result

        