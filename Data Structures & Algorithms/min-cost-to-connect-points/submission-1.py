class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # first create all edges (n^2)
        # need a visit set and a frontier (max heap) and a totalDistance to get to this point
        # we consider it complete when the visit set == number of nodes

        #first we build our adjacency list by calculating the manhattan distance to every other point
        N = len(points)
        adj = {i:[] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))

        pq = [(0,0)] # start from distance of 0, and node 0
        visit = set() # end when all points are connected (i.e N == size of visit)
        totDist = 0
        while len(visit) < N:
            currDist, node = heapq.heappop(pq) # select closest node in frontier
            if node in visit: # if we've already visited, continue
                continue
            totDist += currDist
            visit.add(node)
            for dist2n, n2 in adj[node]: # calculate distances to all unvisited neighbors
                if n2 not in visit:
                    heapq.heappush(pq, (dist2n, n2))
        return totDist

