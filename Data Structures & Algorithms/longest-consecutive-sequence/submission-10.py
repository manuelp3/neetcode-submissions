class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        maxcount = 0
        for num in nums:
            if (num - 1 not in hashset):
                count = 0
                while (num + count in hashset):
                    count += 1
                maxcount = max(maxcount, count)
        return maxcount