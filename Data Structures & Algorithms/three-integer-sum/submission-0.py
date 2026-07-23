class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array
        #loop through array, the index is the first one
        # create two pointers starting at the one
        # depending on if the number is too high or too low, increment/decrement the two pointers
        res = []
        nums.sort()
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while j<k:
                curr = nums[i] + nums[j] + nums[k]
                if curr == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j+=1
                    continue;
                elif curr < 0:
                    j += 1
                elif curr > 0:
                    k-=1
        sit = set()
        for i in res:
            sit.add((i[0], i[1], i[2]))
        resul = list(sit)
        fin = []
        for i in resul:
            fin.append(list(i))
        return fin
                