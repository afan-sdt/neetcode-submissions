class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.capacity = k
        self.minheap = []
        for i in nums:
            if len(self.minheap) < k:
                heapq.heappush(self.minheap, i)
            else:
                if i > self.minheap[0]:
                    heapq.heappop(self.minheap)
                    heapq.heappush(self.minheap, i)


    def add(self, val: int) -> int:
        if len(self.minheap) < self.capacity:
            heapq.heappush(self.minheap, val)
        else:
            if val > self.minheap[0]:
                heapq.heappop(self.minheap)
                heapq.heappush(self.minheap, val)
        return self.minheap[0]
        
