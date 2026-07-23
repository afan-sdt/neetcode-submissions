class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def eatBananas(rate: int) -> bool:
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p)/rate)
            if totalTime <= h:
                return True
            else:
                return False

        lower, upper = 1, max(piles)
        lastValidRate = upper
        while lower <= upper:
            mid = lower + (upper - lower) // 2
            if eatBananas(mid):
                upper = mid - 1
                lastValidRate = mid
            else:
                lower = mid + 1
        return lastValidRate