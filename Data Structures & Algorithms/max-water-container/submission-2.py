class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0, len(heights) - 1
        area = 0

        while (start <= end):
            area = max(min(heights[start], heights[end]) * (end - start), area)
            if (heights[start] > heights[end]):
                end-=1
            else:
                start+=1
        return area