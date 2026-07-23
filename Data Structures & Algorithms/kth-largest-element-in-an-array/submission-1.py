class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #first solution: sort and then return the kth solution
        # this is nlogn
        # nums.sort()
        # return nums[-k]

        #second solution is to have a min heap of size k
        #you want a minheap because everything in the heap 
        # is larger than the head i.e there are k elements larger than the head
        heap = []
        
        for i in nums:
            if len(heap) < k:
                heapq.heappush(heap, i)
            else:
                head = heapq.heappop(heap)
                heapq.heappush(heap, max(head, i))
        return heapq.heappop(heap)
