class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        minheap = []
        res = [0] * len(temperatures)
        for i, n in enumerate(temperatures):
            while minheap and n > minheap[0][0]:
                temp = heapq.heappop(minheap)
                res[temp[1]] = i - temp[1]
            heapq.heappush(minheap, (n,i))
        return res