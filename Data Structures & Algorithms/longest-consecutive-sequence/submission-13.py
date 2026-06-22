class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxcount = 0

        for num in numset:
            base = num
            count = 1
            while (base + 1) in numset:
                count += 1
                base += 1
            if count > maxcount:
                maxcount = count
        return maxcount