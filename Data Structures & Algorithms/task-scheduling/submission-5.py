class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #CARIT: Clarify, Approach, Runtime, Implement, Test
        #clarifying: once a task is processed, it can be done after n seconds or n+1 seconds
        #approach: use a maxheap to represent the queue of items that cna be processed
        # the items with the most remaining elements will be next
        # once a task is processed, the next time it can be used again is time + n
        # we can add the cooldown tasks to a queue (FIFO) where once the time reaches its cooldown time we pop
        #do we pop when time == cooldown time or when time > cooldown time? 
        # time == cooldown time

        freq = Counter(tasks)
        pq = []
        for task, frequency in freq.items():
            pq.append(-frequency)
        heapq.heapify(pq)
        cooldown = deque()
        time = 0

        while pq or cooldown:
            if pq:
                left = heapq.heappop(pq)
                left += 1
                if left < 0:
                    cooldown.append([time + n, left])
            if cooldown:
                if time == cooldown[0][0]:
                    t, amount = cooldown.popleft()
                    heapq.heappush(pq, amount)
            time +=1
        return time