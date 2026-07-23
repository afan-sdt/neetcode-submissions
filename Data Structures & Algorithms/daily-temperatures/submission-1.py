class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, n in enumerate(temperatures):
            while stack and n > stack[-1][0]:
                temp = stack.pop()
                res[temp[1]] = i - temp[1]
            stack.append((n,i))
        return res