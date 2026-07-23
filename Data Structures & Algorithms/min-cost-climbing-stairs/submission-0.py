class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #can calculate min cost to get to each step:
        #cost[x] = min(cost[x-1], cost[x-2])
        soFar = cost.copy()
        soFar.append(0)
        for x in range(2, len(soFar)):
            soFar[x] = min(soFar[x-1], soFar[x-2]) + soFar[x]
            print(soFar[x])
        return soFar[len(soFar)-1]