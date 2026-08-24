class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        res = 0
        for i in nums:
            seen.add(i)
        for i in nums:
            if i-1 not in seen:
                length = 1
                while (i + length) in seen:
                    length +=1
                res = max(res, length)
        return res
