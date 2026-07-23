class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if not nums:
            return 0
        count = 1
        max_count = 1
        for i in range(len(nums)-1):
            print (nums[i])
            print(nums[i+1])
            if nums[i] == nums[i+1]:
                continue
            if nums[i] == (nums[i+1]-1):
                count+=1
                print("yes" + str(count))
                if count > max_count:
                    max_count = count
            else:
                count = 1
        return max_count

        