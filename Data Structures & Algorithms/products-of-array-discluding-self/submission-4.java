class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] solution = new int[nums.length];

        solution[0] = 1;
        int product = nums[0];

        for (int i = 1; i < nums.length; i++) {
            solution[i] = product;
            product *= nums[i];
        }

        product = nums[nums.length - 1];

        for (int i = nums.length - 2; i >= 0; i--) {
            solution[i] *= product;
            product *= nums[i];
        }

        return solution;
    }
}  
