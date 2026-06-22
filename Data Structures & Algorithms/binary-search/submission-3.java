class Solution {
    public int search(int[] nums, int target) {
        int low = 0;
        int high = nums.length - 1;
        int mid = (high+low)/2;

        while (nums[mid] != target) {
            if (target > nums[mid]) {
                low = mid + 1;
            }
            else {
                high = mid - 1;
            }
            mid = (low+high)/2;
            if (low > high) {
                return -1;
            }
        }
        return mid;
    }
}
