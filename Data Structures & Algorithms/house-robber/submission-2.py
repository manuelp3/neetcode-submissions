class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_set = {}
        def helper(i):
            if i >= len(nums):
                return 0
            if i in rob_set:
                return rob_set[i]
            rob = nums[i] + helper(i + 2)
            no_rob = helper(i + 1)
            rob_set[i] = max(rob, no_rob)
            return rob_set[i]
        return helper(0)