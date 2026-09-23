class Solution:
    def rob(self, nums: List[int]) -> int:
        count = {}
        def helper(index):
            if index >= len(nums):
                return 0
            if index in count:
                return count[index]
            rob = nums[index] + helper(index + 2)
            no_rob = helper(index + 1)
            best = max(rob, no_rob)
            count[index] = best
            return best
        return helper(0)