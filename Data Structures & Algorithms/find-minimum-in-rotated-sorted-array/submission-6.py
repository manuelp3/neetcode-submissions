class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        minimum = nums[start]

        while (start <= end):
            mid = (start + end) // 2
            if (nums[mid] >= nums[start]):
                minimum = min(minimum, nums[start])
                start = mid + 1
            else:
                minimum = min(minimum, nums[mid])
                end = mid - 1
        return minimum