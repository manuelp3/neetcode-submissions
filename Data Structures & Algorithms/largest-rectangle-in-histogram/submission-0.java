class Solution {
    public int largestRectangleArea(int[] heights) {
        int maxArea = 0;
        Stack<int[]> stack = new Stack<>();

        for (int i = 0; i < heights.length; i++) {
            int start = i;

            while (!stack.isEmpty() && stack.peek()[1] > heights[i]) {
                int[] pair = stack.pop();
                maxArea = Math.max(maxArea, (i - pair[0]) * pair[1]);
                start = pair[0];
            }

            //maxArea = Math.max(maxArea, heights[i] * start);

            stack.push(new int[]{start, heights[i]});
        }

        while (!stack.isEmpty()) {
            int[] pair = stack.pop();
            maxArea = Math.max(maxArea, (heights.length - pair[0]) * pair[1]);
        }
        return maxArea;
    }
}
