class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pre = 1
        test = [1] * n

        for i in range(1, n):
            test[i] = nums[i - 1] * pre
            pre *= nums[i - 1]
        
        post = 1

        for i in range(n - 2, -1, -1):
            test[i] *= nums[i + 1] * post
            post *= nums[i + 1]
        
        return test
