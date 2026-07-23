class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #when it comes to frequency you can have a frequency hashmap 
        #and then you can sort by frequency to get the most
        # but the best would probably be to heapify the values array
        myMap = defaultdict(int)
        for n in nums:
            myMap[n]+=1
        data = []
        for key, value in myMap.items():
            data.append((value, key))
        heep = [(-val, key) for (val, key) in data]
        heapq.heapify(heep)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heep)[1])
        return res
