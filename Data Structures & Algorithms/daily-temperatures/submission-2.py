class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stck = []
        res = [0] * len(temperatures)
        for currIndex, currTemp in enumerate(temperatures):
            while stck and currTemp > stck[-1][0]:
                temp = stck.pop()
                res[temp[1]] = currIndex - temp[1]
            stck.append((currTemp, currIndex))
        return res
