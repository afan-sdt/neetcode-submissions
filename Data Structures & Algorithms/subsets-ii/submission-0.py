class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        subsets.append([])
        #for each number, going to add it 
        nums.sort()
        endIndex = 0
        for index in range(len(nums)):
            startIndex = 0
            if index > 0 and nums[index] == nums[index-1]:
                startIndex = endIndex
            endIndex = len(subsets)
            # thisRow = []
            for subs in range(startIndex, endIndex):
                curr = list(subsets[subs]) #creates copy
                curr.append(nums[index])
                subsets.append(curr)
            # subsets += thisRow
        return subsets
                

