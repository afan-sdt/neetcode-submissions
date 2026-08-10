class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        two = cost[0]
        one = cost[1]
        for i in range(2, n):
            print(one)
            tmp = one
            one = min(one, two) + cost[i]
            two = tmp
        print(one, two)
        return min(one, two)