class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [(x,y) for x, y in zip(position, speed)]
        arr.sort()
        stck = []
        for i in reversed(arr):
            stck.append((target-i[0])/i[1])
            if len(stck)>=2 and stck[-1] <= stck[-2]:
                stck.pop()
        return len(stck)