class Solution {
    public int trap(int[] height) {
        int start = 0;
        int end = height.length - 1;

        int maxLeft = height[start];
        int maxRight = height[end];
        int total = 0;

        while (start <= end) {
            if (maxLeft < maxRight) {
                total += Math.max(0, (Math.min(maxLeft, maxRight) - height[start]));
                maxLeft = Math.max(height[start], maxLeft);
                start++;
            }
            else {
                total += Math.max(0, (Math.min(maxLeft, maxRight) - height[end]));
                maxRight = Math.max(height[end], maxRight);
                end--;
            }
        }
        return total;
    }
}
