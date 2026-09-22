class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # CARIT: clarify, approach, runtime, implement, test

        # k is the starting node 
        #approach: create adjList with weights, create a pq that selects your next, and a visited list of nodes that we have set distance for
        # 
        dist = [float("inf")] * n
        pq = []
        visited = set()
        adjList = {i:[] for i in range(n)}
        dist[k-1] = 0

        for src, dest, weight in times:
            adjList[src-1].append((dest-1, weight))
        heapq.heappush(pq, (0, k-1))

        while pq:
            currDist, curr = heapq.heappop(pq)
            if curr in visited:
                continue
            visited.add(curr)
            for dest, d2n in adjList[curr]:
                if dest in visited:
                    continue
                heapq.heappush(pq, (d2n + currDist, dest) )
                dist[dest] = min(dist[dest], d2n + currDist)
        return max(dist) if len(visited) == n else -1