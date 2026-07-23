class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones2 = [x*-1 for x in stones]
        heapq.heapify(stones2)
        #create heap

        #loop while stones has more than one 
        while(len(stones2) > 1):
            #pop 2 off the heap
            temp1 = heapq.heappop(stones2)
            temp2 = heapq.heappop(stones2)
            #subtract
            diff = abs(temp1-temp2)
            #absolute value of difference goes back in
            if diff > 0:
                heapq.heappush(stones2, -1 * diff)
        if stones2:
            return -1 * stones2[0]
        return 0
