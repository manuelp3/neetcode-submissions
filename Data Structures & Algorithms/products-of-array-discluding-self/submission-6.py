class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        prefix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = nums[i - 1] * pre
            pre *= nums[i - 1]
        
        post = 1
        postfix = [1] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = nums[i + 1] * post
            post *= nums[i + 1]
        
        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] = prefix[i] * postfix[i]
        return res
