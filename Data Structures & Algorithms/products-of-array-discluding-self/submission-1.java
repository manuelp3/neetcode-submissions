class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] solution = new int[nums.length];
        int[] prefix = new int[nums.length];
        int[] postfix = new int[nums.length];

        prefix[0] = 1;
        int product = nums[0];

        for (int i = 1; i < nums.length; i++) {
            prefix[i] = product;
            product *= nums[i];
        }

        postfix[nums.length - 1] = 1;
        product = nums[nums.length - 1];

        for (int i = nums.length - 2; i >= 0; i--) {
            postfix[i] = product;
            product *= nums[i];
        }

        for (int i = 0; i < nums.length; i++) {
            solution[i] = prefix[i] * postfix[i];
        }

        return solution;
    }
}  
