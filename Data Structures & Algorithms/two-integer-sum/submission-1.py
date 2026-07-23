class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for i, n in enumerate(nums):
            if n in myMap:
                return [myMap[n], i]
            myMap[target-n] = i
        