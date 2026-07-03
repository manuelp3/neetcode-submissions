class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        max_area = 0

        while (start < end):
            area = min(heights[start], heights[end]) * (end - start)
            max_area = max(max_area, area)
            if (heights[start] > heights[end]):
                end -= 1
            else:
                start += 1
        return max_area