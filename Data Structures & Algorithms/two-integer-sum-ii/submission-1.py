class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            added = numbers[left] + numbers[right]
            if added > target:
                # decrement right
                right -= 1
            elif added < target:
                #increment left
                left += 1
            else:
                #true return indixes
                return[left + 1, right + 1]
        return []