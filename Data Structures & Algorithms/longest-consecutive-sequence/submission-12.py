class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        if not nums:
            return 0
        count = 1
        for value in nums:
            length = 1
            if (value - 1 not in nums):
                while (value + 1 in nums):
                    length += 1
                    value += 1
                count = max(count, length)
        return count
