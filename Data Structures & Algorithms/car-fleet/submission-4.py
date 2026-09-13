class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #sort by position then we see if arrival time of a <= arrival time of b
        # t = 10
        # 0, 1, 4, 7  position
        # 1, 2, 2, 1 speed
        # 10s 5s 3s 3s
        # 
        # go in reversed order + add eta to stack
        # if the current end time is > top of stack, append it, otherwise ignore 
        # this is because if the end time is <=, it will arrive as part of the previous fleet
        #               | <-target
        # car car car 
        tups = list(zip(position, speed))
        tups.sort(reverse=True)
        stck = []
        for p , s in tups:
            endTime = (target - p) / s
            if stck and endTime <= stck[-1]:
                continue
            stck.append(endTime) 
        return len(stck)
