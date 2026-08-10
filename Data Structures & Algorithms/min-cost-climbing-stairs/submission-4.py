class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        two = cost[0]
        one = cost[1]
        for i in range(2, n):
            tmp = one
            one = min(one, two) + cost[i]
            two = tmp
        return min(one, two)