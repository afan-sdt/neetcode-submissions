class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build an adj list
        # keep a visited set
        # keep a pq of all nodes in our frontier

        adj = {i: [] for i in range(n)}
        for u, v, w in times:
            adj[u-1].append((v-1,w))
        pq = []
        heapq.heappush(pq, (0, k-1)) # the priority que sorts by distance
        visit = set() # set of visited nodes
        dist = [float('inf')] * n
        dist[k-1] = 0
        while pq:
            t1, n1 = heapq.heappop(pq)
            if n1 in visit:
                continue
            for n2, t2 in adj[n1]:
                if n2 in visit:
                    continue
                heapq.heappush(pq, (t1 + t2, n2)) # add new node to frontier
                dist[n2] = min(dist[n2], t1+t2 ) # update if this is best distance seensoFar
            visit.add(n1) # explored all its neighbors, should be min
        
        return max(dist) if len(visit) == n else -1

        
