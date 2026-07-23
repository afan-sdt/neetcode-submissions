class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(heights)-1
        while left < right:
            area = (right-left) * min(heights[left], heights[right])
            if maxArea < area:
                maxArea = area
            if heights[right] > heights[left]:
                left+=1
            else:
                right -=1
        return maxArea
        