class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort array
        sortedNums = sorted(nums)
        res = []
        #iterate through the sorted array
        for i in range(len(sortedNums)):
            #try to find two values in rest where y + z = -x
            if i > 0 and sortedNums[i-1] == sortedNums[i]:
                continue
            left, right = i+1, len(sortedNums) - 1
            while left < right:
                if sortedNums[left] + sortedNums[right] + sortedNums[i] == 0:
                    res.append([sortedNums[left], sortedNums[right], sortedNums[i]])
                    left +=1
                    while left < right and sortedNums[left] == sortedNums[left-1]:
                        left += 1
                    right -= 1
                    while left < right and sortedNums[right] == sortedNums[right+1]:
                        right -=1
                elif sortedNums[left] + sortedNums[right] + sortedNums[i] > 0:
                    right -=1
                elif sortedNums[left] + sortedNums[right] + sortedNums[i] < 0:
                    left +=1
        return res