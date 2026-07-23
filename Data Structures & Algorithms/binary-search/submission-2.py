class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binary_search(left: int, right: int):
            middle = (left + right)//2
            print(nums[middle])
            if(nums[middle] == target):
                return middle
            elif(right-left<=1):
                return -1
            elif(nums[middle] < target):
                return binary_search(middle, right)
            elif(nums[middle] > target):
                return binary_search(left, middle)

        return binary_search(0, len(nums))
