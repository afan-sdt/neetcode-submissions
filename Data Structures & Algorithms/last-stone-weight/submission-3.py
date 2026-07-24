class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # we want to have a maxheap containing the stones
        # each step we grab 2 biggest stones
        #if equal,  we continue
        #if one is more, we subtract and push the remainder into the maxheap
        # if nothing left , return 0
        # if 1 left, return that
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            rock1 = heapq.heappop(maxHeap)
            rock2 = heapq.heappop(maxHeap)
            diff = rock1-rock2
            print(rock1, rock2, diff)
            if diff < 0:
                heapq.heappush(maxHeap, diff)
        return -maxHeap[0] if maxHeap else 0