class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        indexed = []
        #create tuple list
        for index, value in enumerate(points):
            heapq.heappush(indexed,(-math.sqrt(value[0]**2 + value[1]**2), index))
            if len(indexed) > k:
                heapq.heappop(indexed)
        return [points[x[1]] for x in indexed]