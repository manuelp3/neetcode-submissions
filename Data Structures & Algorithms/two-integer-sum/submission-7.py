class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for i in range(0, len(nums)):
            my_dict[nums[i]] = i
        
        for i in range(0, len(nums)):
            value = target - nums[i]
            if value in my_dict and my_dict[value] != i:
                return [i, my_dict[value]]
            