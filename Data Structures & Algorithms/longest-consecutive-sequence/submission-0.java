class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        int count = 0;
        int max = 0;
        //int min = nums[0];

        for (int i = 0; i < nums.length; i++) {
            set.add(nums[i]);
            //if (nums[i] < min) min = nums[i];
        }

        // while (set.contains(min)) {
        //     count++;
        //     min++;
        // }

        for (int i = 0; i < nums.length; i++) {
            int test = nums[i];
            count = 0;
            while (set.contains(test)) {
                count++;
                test++;
                if (count > max) {
                    max = count;
                }
            }
        }
        return max;
    }
}
