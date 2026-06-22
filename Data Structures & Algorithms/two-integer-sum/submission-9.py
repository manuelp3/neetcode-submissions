class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        adders = {}
        for i in range(len(nums)):
            adders[target - nums[i]] = i
        
        print(adders)
        
        for i in range(len(nums)):
            if nums[i] in adders:
                if i == adders[nums[i]]:
                    continue
                return [i, adders[nums[i]]]