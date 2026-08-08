class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i:[] for i in range(n)}
        for src1, dst1, cost1 in flights:
            adj[src1].append((dst1, cost1))
        
        # Track stops taken to reach a node to allow revisiting with fewer stops
        stops_to_node = [float('inf')] * n
        pq = [(0, 0, src)] # (cost, stops, node)
        
        while pq:
            currCost, stops, node = heapq.heappop(pq)
            
            if node == dst:
                return currCost
            
            # If we've reached this node before with fewer or equal stops, skip
            if stops > k or stops >= stops_to_node[node]:
                continue
            
            stops_to_node[node] = stops
            
            for nei, neiCost in adj[node]:
                heapq.heappush(pq, (neiCost + currCost, stops + 1, nei))
        
        return -1