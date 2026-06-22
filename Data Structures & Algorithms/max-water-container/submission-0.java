class Solution {
    public int maxArea(int[] heights) {
        int start = 0;
        int end = heights.length - 1;
        int max = 0;

        while (start < end) {
            int val = Math.min(heights[start], heights[end]) * (end - start);

            if (val > max) {
                max = val;
            }
            if (heights[start] <= heights[end]) {
                start++;
            }
            else {
                end--;
            }
        }
        return max;
    }
}
