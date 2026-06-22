class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(0,(len(nums))):
            dict.update({nums[i] : i})
        for i in range(0,(len(nums))):
            diff = target - nums[i]
            if (diff in dict and dict[diff] != i):
                    return [i, dict[diff]]