class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solution = [1] * len(nums)

        for i in range(1, len(nums)):
            solution[i] = solution[i - 1] * nums[i - 1]

        product = 1
        
        for i in range(len(nums) - 2, -1, -1):
            product *= nums[i + 1]
            solution[i] *= product

        return solution
        