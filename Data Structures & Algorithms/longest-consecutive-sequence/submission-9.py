class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        hashset = set(nums)

        maxcount = 1
        for num in nums:
            if (num - 1 not in hashset):
                count = 0
                while (num + count in hashset):
                    count += 1
                maxcount = max(maxcount, count)
        return maxcount