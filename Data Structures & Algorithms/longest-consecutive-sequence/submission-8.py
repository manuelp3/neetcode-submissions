class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        for num in nums:
            hashset.add(num)

        if not nums:
            return 0

        maxcount = 1
        for num in nums:
            if (num - 1 not in hashset):
                number = num
                count = 1
                while (number + 1 in hashset):
                    count += 1
                    number += 1
                    maxcount = max(maxcount, count)
        return maxcount