class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        count = 0
        maxCount = 0
        
        for item in nums:
            value = item
            while (value) in hashset:
                count+=1
                value+=1
            maxCount = max(count, maxCount)
            count = 0
        return maxCount