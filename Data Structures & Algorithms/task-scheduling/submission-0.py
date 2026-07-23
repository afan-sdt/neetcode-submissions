class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #turn list into a deque
        time = 0
        freq = {}
        for t in tasks:
            if t in freq:
                freq[t] +=1
            else:
                freq[t] = 1
        mxheep=[-cnt for cnt in freq.values()]
        heapq.heapify(mxheep)
        que = deque() #add to queue time,-cnt
        while que or mxheep:
            time += 1
            if mxheep:
                rem = heapq.heappop(mxheep)
                rem += 1
                if rem < 0:
                    que.append([time + n, rem])
            if que and que[0][0] <= time:
                topel = que.popleft()
                heapq.heappush(mxheep,topel[1])
        return time
