class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        print(nums)
        for i in range(len(nums)):
            if (nums[i] > 0):
                break
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            start = i + 1
            end = len(nums) - 1
            while (start < end):
                sums = nums[start] + nums[end] + nums[i]
                if sums < 0:
                    start += 1
                if sums > 0:
                    end -= 1
                if sums == 0:
                    res.append([nums[start], nums[i], nums[end]])
                    start += 1
                    end -= 1
                    while (start < len(nums) and nums[start] == nums[start - 1]):
                        start += 1
        return res