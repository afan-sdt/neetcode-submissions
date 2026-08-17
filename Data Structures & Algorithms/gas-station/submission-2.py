class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # gas is gas at station
        # cost is needed to get to next
        # sum of cost should be less than or equal to sum of gas
        # add up costs and gas as you iterate
        # if the final result is negative, not possible
        # if positive, the index it became positive and never became negative again is the start index
        if sum(gas) < sum(cost):
            return -1
        firstPositive = 0
        totalSum = 0
        n = len(gas)
        for i in range(n):
            totalSum += (gas[i] - cost[i])

            print(totalSum)
            if totalSum < 0:
                totalSum = 0
                firstPositive = i+1
        return firstPositive