class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();

        for (int i = 0; i < nums.length; i++) {
            set.add(nums[i]);
        }

        int count = 0;
        int max = 0;

        for (int num : set) {
            if (!set.contains(num - 1)) {
                int test = num;
                count = 0;
                while (set.contains(test)) {
                    count++;
                    test++;
                }
                if (count > max) {
                    max = count;
                }
            }
        }
        return max;
    }
}
