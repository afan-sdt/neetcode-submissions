class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #we build an adjacency list mapping each node to its neighbors and weights
        adjList = defaultdict(list)

        for u, v, w in times:
            adjList[u].append((v,w))
        #we create a minheap with (weight, node)
        # we add our initial node to our queue with (0, k)
        minHeap = [(0,k)]

        visited = set()
        t = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = max(t, w1)
            for n2, w2 in adjList[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w2 + w1, n2))
        
        return t if len(visited) == n else -1
