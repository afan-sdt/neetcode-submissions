class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums # by default, python stores minheat
        self.k = k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        #compare to top of minheap of size k
        # if less, we can ignore since won't be in top k elements
        #if greater, remove the top, insert into array
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]