class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = [] # by default, python stores minheat
        self.k = k
        for i in nums:
            self.add(i)

    def add(self, val: int) -> int:
        #compare to top of minheap of size k
        # if less, we can ignore since won't be in top k elements
        #if greater, remove the top, insert into array
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
        elif len(self.minHeap) == self.k:
            if val > self.minHeap[0]:
                heapq.heappop(self.minHeap)
                heapq.heappush(self.minHeap, val)
        return self.minHeap[0]

        
