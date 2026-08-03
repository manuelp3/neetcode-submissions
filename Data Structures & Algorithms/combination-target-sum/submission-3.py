class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(index, current, total):
            #print(index, current, total)
            if total == target:
                res.append(current.copy())
                return
            if index >= len(nums) or total > target:
                return
            current.append(nums[index])
            helper(index, current, total + nums[index])
            current.pop()
            helper(index + 1, current, total)
        helper(0,[],0)
        return res