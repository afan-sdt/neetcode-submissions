class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        res = 0
        for i in nums:
            seen.add(i)
        for i in nums:
            length = 1
            if i in seen:
                temp = i+1
                seen.remove(i)
                while temp in seen:
                    length +=1
                    seen.remove(temp)
                    temp += 1
                temp = i - 1
                while temp in seen:
                    length +=1
                    seen.remove(temp)
                    temp -= 1
            res = max(res, length)
        return res
