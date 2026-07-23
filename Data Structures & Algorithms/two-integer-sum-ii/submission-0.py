class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        high = len(numbers) - 1
        low = 0
        while((numbers[high]+numbers[low]) != target):
            if((numbers[high] + numbers[low]) > target ):
                high -= 1
            elif((numbers[high] + numbers[low] < target)):
                low += 1
        return [low+1, high+1]
        