class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while (start <= end):
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            if (nums[mid] >= nums[start]):
                if (target < nums[start] or target > nums[mid]):
                    #search through right array
                    start = mid + 1
                else:
                    #search through left array
                    end = mid - 1
            else:
                if (target > nums[end] or target < nums[mid]):
                    #search through left array
                    end = mid - 1
                else:
                    #search through right array
                    start = mid + 1
        return -1